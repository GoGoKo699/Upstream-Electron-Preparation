# Scientific checks and infrastructure

The three original scientific suites are active flat copies, with no code or assertion changes:

| Command (use a new output file) | Groups | Saved report |
|---|---:|---|
| `python checks/check_pulse_reachability.py --output NEW.json` | 6 | `results/exact_reachability.json` |
| `python checks/check_finite_accuracy.py --output NEW.json` | 7 | `results/finite_fidelity.json` |
| `python checks/check_control_audit.py --output NEW.json` | 5 | `results/calibration_duration.json` |

`control_integrals.py` is the unchanged helper. Its historical insertion of a `prior` search path is inert in this flat directory; `check_finite_accuracy.py` resolves beside it. This preserves all four source hashes rather than changing numerical code merely for an import.

Use `python verify.py --output-dir NEW_DIRECTORY` for complete logs, integrity and comparison records. `test_repository.py` tests the new runner/record layer; it is not an additional scientific theorem or part of the 18 groups.

The preserved scripts refer to their original SCOUT notes in diagnostic strings. The live proof route is research/MODEL_AND_CLAIMS.md; the corresponding original notes are byte-preserved under archive/scouts/scout10/. These diagnostic strings are not evidence of new work or a missing dependency.
