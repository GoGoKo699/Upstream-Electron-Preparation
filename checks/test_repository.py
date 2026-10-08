#!/usr/bin/env python3
"""Eight tests of the repository/verification layer, separate from scientific groups."""
from pathlib import Path
import hashlib
import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("uep_verify", ROOT / "verify.py")
verify = importlib.util.module_from_spec(spec)
spec.loader.exec_module(verify)


class RepositoryTests(unittest.TestCase):
    def test_protected_sources_and_license(self):
        result = verify.check_imports()
        self.assertEqual(result["status"], "PASS", result)
        self.assertEqual(result["protected_files"], 83)
        for archive in (ROOT / "archive/scouts/scout10", ROOT / "archive/readiness"):
            original = json.loads((archive / "MANIFEST.json").read_text())
            for name, meta in original.items():
                self.assertEqual(hashlib.sha256((archive / name).read_bytes()).hexdigest(), meta["sha256"])

    def test_import_mutation_is_not_silently_accepted(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "provenance").mkdir()
            (root / "a.txt").write_bytes(b"changed")
            expected = {"files": {"a.txt": {"sha256": verify.digest(b"original"), "bytes": 8}}}
            (root / "provenance/IMPORT_MANIFEST.json").write_text(json.dumps(expected))
            self.assertEqual(verify.check_imports(root)["status"], "FAIL")

    def test_exact_and_close_float_records(self):
        self.assertEqual(verify.compare({"x": [1.0, 2]}, {"x": [1.0, 2]}), [])
        rows = verify.compare({"x": 1.0}, {"x": 1.0 + 1e-11})
        self.assertEqual(len(rows), 1)
        self.assertTrue(rows[0]["accepted"])
        self.assertFalse(verify.compare(1.0, 1.01)[0]["accepted"])

    def test_structure_counts_booleans_and_nonfinite(self):
        for a, b in ((1, 2), (True, 1), (1, 1.0), ([1], [1, 2]), ({"a": 1}, {"b": 1}), (float("nan"), float("nan")), (float("inf"), float("inf"))):
            self.assertTrue(any(not row["accepted"] for row in verify.compare(a, b)))

    def test_active_navigation_and_forbidden_extensions(self):
        result = verify.integrity()
        self.assertEqual(result["status"], "PASS", result)
        self.assertGreater(result["links"]["checked"], 30)
        self.assertFalse(result["forbidden_source_files"])

    def test_existing_output_is_refused_without_edits(self):
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp)
            marker = p / "marker.txt"
            marker.write_bytes(b"keep")
            result = subprocess.run([sys.executable, str(ROOT / "verify.py"), "--output-dir", str(p)], cwd=ROOT, capture_output=True, text=True)
            self.assertEqual(result.returncode, 2)
            self.assertEqual(marker.read_bytes(), b"keep")
            self.assertEqual(list(p.iterdir()), [marker])

    def test_exact_source_snapshot_contains_new_files(self):
        snap = verify.snapshot()
        for name in ("README.md", ".github/MAINTENANCE.md", "verify.py", "checks/check_finite_accuracy.py", "results/finite_fidelity.json", "literature/CABART_2018_COMPARISON.md"):
            self.assertEqual(snap[name], verify.digest((ROOT / name).read_bytes()))

    def test_safe_import_paths_and_fixed_scientific_count(self):
        self.assertTrue(verify.safe_relative("checks/example.py"))
        self.assertFalse(verify.safe_relative("../outside"))
        self.assertFalse(verify.safe_relative("/tmp/outside"))
        self.assertFalse(verify.safe_relative(".git/config"))
        self.assertEqual(sum(count for _, _, count in verify.SUITES), 18)
        self.assertEqual(len(verify.SUITES), 3)


if __name__ == "__main__":
    unittest.main(verbosity=2)
