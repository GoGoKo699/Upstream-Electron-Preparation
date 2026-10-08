#!/usr/bin/env python3
"""Run the fixed scientific suites with preserved references and full differences.

python verify.py --integrity-only
python verify.py --output-dir NEW_DIRECTORY

Standard library only in this runner. The original suites use requirements.txt.
No reference, original source, or existing evidence directory is overwritten.
"""
from __future__ import annotations
import argparse
from datetime import datetime, timezone
import hashlib
import json
import math
import os
from pathlib import Path
import re
import subprocess
import sys
import time
import zipfile

ROOT = Path(__file__).resolve().parent
POLICY = {"float_relative_tolerance": 1e-9, "float_absolute_tolerance": 5e-10,
          "integers_booleans_strings_structure": "exact", "nonfinite": "reject"}
SUITES = (
    ("exact_reachability", "check_pulse_reachability.py", 6),
    ("finite_fidelity", "check_finite_accuracy.py", 7),
    ("calibration_duration", "check_control_audit.py", 5),
)


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def write_json(path: Path, value: object) -> None:
    with path.open("x", encoding="utf-8") as handle:
        json.dump(value, handle, indent=2, sort_keys=True, allow_nan=False)
        handle.write("\n")


def git_value(root: Path, *args: str) -> str | None:
    proc = subprocess.run(["git", *args], cwd=root, capture_output=True, text=True)
    return proc.stdout.strip() if proc.returncode == 0 else None


def source_paths(root: Path) -> list[str]:
    # Tracked files define the exact source snapshot; generated evidence is not source.
    proc = subprocess.run(["git", "ls-files", "-z"], cwd=root, capture_output=True)
    if proc.returncode == 0 and proc.stdout:
        return sorted(proc.stdout.decode().rstrip("\0").split("\0"))
    excluded = {".git", ".venv", "__pycache__", "verification-artifacts"}
    return sorted(p.relative_to(root).as_posix() for p in root.rglob("*")
                  if p.is_file() and not set(p.relative_to(root).parts) & excluded
                  and not any(part.startswith("local-evidence") for part in p.relative_to(root).parts))


def snapshot(root: Path = ROOT) -> dict[str, str]:
    return {name: digest((root / name).read_bytes()) for name in source_paths(root)}


def safe_relative(name: str) -> bool:
    p = Path(name)
    return bool(name) and not p.is_absolute() and ".." not in p.parts and ".git" not in p.parts


def check_imports(root: Path = ROOT) -> dict[str, object]:
    manifest = json.loads((root / "provenance/IMPORT_MANIFEST.json").read_text())
    failures = []
    for name, expected in manifest["files"].items():
        if not safe_relative(name):
            failures.append({"path": name, "reason": "unsafe path"})
            continue
        path = root / name
        if not path.is_file() or path.is_symlink():
            failures.append({"path": name, "reason": "missing or nonregular file"})
            continue
        data = path.read_bytes()
        if len(data) != expected["bytes"] or digest(data) != expected["sha256"]:
            failures.append({"path": name, "reason": "protected bytes differ"})
    return {"status": "PASS" if not failures else "FAIL",
            "protected_files": len(manifest["files"]), "failures": failures}


def check_links(root: Path = ROOT) -> dict[str, object]:
    files = list(root.glob("*.md"))
    if (root / "llms.txt").is_file():
        files.append(root / "llms.txt")
    for folder in ("research", "literature", "tutorial", ".github", "checks", "results"):
        files.extend((root / folder).glob("*.md"))
    failures, count = [], 0
    for path in files:
        text = re.sub(r"```.*?```", "", path.read_text(), flags=re.S)
        for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", text):
            if re.match(r"(?:[a-zA-Z]+:|#)", target):
                continue
            target = target.split("#", 1)[0]
            if not target:
                continue
            count += 1
            resolved = (path.parent / target).resolve()
            if not resolved.is_relative_to(root.resolve()) or not resolved.exists():
                failures.append({"file": str(path.relative_to(root)), "target": target})
    return {"status": "PASS" if not failures else "FAIL", "checked": count, "failures": failures}


def integrity(root: Path = ROOT) -> dict[str, object]:
    imported, links = check_imports(root), check_links(root)
    forbidden = [p for p in source_paths(root) if Path(p).suffix.lower() in
                 {".pdf", ".ttf", ".otf", ".woff", ".woff2", ".pyc"}]
    return {"status": "PASS" if imported["status"] == links["status"] == "PASS" and not forbidden else "FAIL",
            "imports": imported, "links": links, "forbidden_source_files": forbidden}


def compare(reference: object, observed: object, path: str = "$") -> list[dict[str, object]]:
    differences: list[dict[str, object]] = []
    if isinstance(reference, dict) and isinstance(observed, dict):
        for key in sorted(reference.keys() | observed.keys()):
            if key not in reference or key not in observed:
                differences.append({"path": f"{path}.{key}", "kind": "key", "accepted": False,
                                    "reference": reference.get(key), "observed": observed.get(key)})
            else:
                differences += compare(reference[key], observed[key], f"{path}.{key}")
    elif isinstance(reference, list) and isinstance(observed, list):
        if len(reference) != len(observed):
            differences.append({"path": path, "kind": "length", "accepted": False,
                                "reference": len(reference), "observed": len(observed)})
        else:
            for i, (a, b) in enumerate(zip(reference, observed)):
                differences += compare(a, b, f"{path}[{i}]")
    elif type(reference) is not type(observed):
        differences.append({"path": path, "kind": "type", "accepted": False,
                            "reference": reference, "observed": observed})
    elif isinstance(reference, float):
        finite = math.isfinite(reference) and math.isfinite(observed)
        if not finite or reference != observed:
            accepted = finite and math.isclose(reference, observed,
                          rel_tol=POLICY["float_relative_tolerance"],
                          abs_tol=POLICY["float_absolute_tolerance"])
            differences.append({"path": path, "kind": "float", "accepted": accepted,
                "reference": reference if math.isfinite(reference) else repr(reference),
                "observed": observed if math.isfinite(observed) else repr(observed),
                "absolute_difference": abs(reference - observed) if finite else None})
    elif reference != observed:
        differences.append({"path": path, "kind": "exact", "accepted": False,
                            "reference": reference, "observed": observed})
    return differences


def run_all(output: Path) -> int:
    if output.exists():
        raise FileExistsError(f"Refusing existing output directory: {output}")
    before_source = snapshot()
    output.mkdir(parents=True)
    before = integrity()
    write_json(output / "integrity-before.json", before)
    write_json(output / "source-sha256.json", before_source)
    report: dict[str, object] = {
        "status": "RUNNING", "repository": "GoGoKo699/Upstream-Electron-Preparation",
        "commit": git_value(ROOT, "rev-parse", "HEAD"),
        "tree": git_value(ROOT, "write-tree"),
        "source_file_count": len(before_source), "comparison_policy": POLICY,
        "before": before, "suite_count": 3, "tests_expected": 18, "runs": [],
    }
    env = dict(os.environ, OPENBLAS_NUM_THREADS="1", OMP_NUM_THREADS="1",
               PYTHONDONTWRITEBYTECODE="1", TERM="dumb")
    write_json(output / "environment.json", {
        "python": sys.version, "platform": sys.platform,
        "started_utc": datetime.now(timezone.utc).isoformat(),
        "blas_threads": 1, "pythonhashseed": os.environ.get("PYTHONHASHSEED"),
        "dependencies": subprocess.check_output([sys.executable, "-m", "pip", "freeze"], text=True).splitlines(),
    })
    for name, script, expected in SUITES:
        folder = output / name
        folder.mkdir()
        reference = (ROOT / "results" / f"{name}.json").read_bytes()
        (folder / "reference.json").write_bytes(reference)
        start = time.monotonic()
        with (folder / "execution.log").open("x") as log:
            result = subprocess.run([sys.executable, str(ROOT / "checks" / script),
                        "--output", str(folder / "observed.json")], cwd=ROOT, env=env,
                        stdout=log, stderr=subprocess.STDOUT)
        observed_path = folder / "observed.json"
        try:
            raw = observed_path.read_bytes()
            observed = json.loads(raw)
            fields = compare(json.loads(reference), observed)
            assertions = result.returncode == 0 and observed.get("status") == "PASS" and observed.get("tests_run") == expected
            byte_equal = raw == reference
        except (OSError, ValueError) as error:
            observed, raw, assertions, byte_equal = {}, b"", False, False
            fields = [{"path": "$", "kind": "report", "accepted": False, "error": str(error)}]
        agreement = all(row["accepted"] for row in fields)
        comparison = {"agreement": agreement, "byte_identical": byte_equal,
                      "reference_sha256": digest(reference), "observed_sha256": digest(raw),
                      "difference_count": len(fields), "differences": fields, "policy": POLICY}
        write_json(folder / "comparison.json", comparison)
        report["runs"].append({"name": name, "exit_code": result.returncode,
             "tests_expected": expected, "tests_run": observed.get("tests_run"),
             "scientific_assertions_passed": assertions, "numerical_agreement": agreement,
             "byte_identical": byte_equal, "difference_count": len(fields),
             "seconds": time.monotonic() - start})
        print(f"{name}: assertions={assertions}; agreement={agreement}; byte_equal={byte_equal}", flush=True)
    after_source, after = snapshot(), integrity()
    write_json(output / "integrity-after.json", after)
    report["after"] = after
    report["source_unchanged"] = before_source == after_source
    report["all_reference_bytes_identical"] = all(row["byte_identical"] for row in report["runs"])
    passed = (before["status"] == after["status"] == "PASS" and report["source_unchanged"]
              and all(row["scientific_assertions_passed"] and row["numerical_agreement"] for row in report["runs"]))
    report["status"] = "PASS" if passed else "FAIL"
    with zipfile.ZipFile(output / "tracked-source.zip", "x", zipfile.ZIP_DEFLATED) as archive:
        archive.comment = json.dumps({"commit": report["commit"], "tree": report["tree"]}).encode()
        for name in sorted(before_source):
            archive.write(ROOT / name, name)
    write_json(output / "REPORT.json", report)
    print(f"{report['status']}: 3 suites / 18 scientific groups; source_unchanged={report['source_unchanged']}")
    return 0 if passed else 1


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--integrity-only", action="store_true")
    group.add_argument("--output-dir", type=Path)
    args = parser.parse_args()
    if args.integrity_only:
        result = integrity()
        print(json.dumps(result, indent=2, sort_keys=True))
        raise SystemExit(0 if result["status"] == "PASS" else 1)
    try:
        raise SystemExit(run_all(args.output_dir.resolve()))
    except FileExistsError as error:
        parser.error(str(error))


if __name__ == "__main__":
    main()
