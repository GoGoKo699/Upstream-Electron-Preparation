# Scientific checks and infrastructure

The scientific suites check reachability, finite-fidelity optimization, and the nominal optimizer's calibration and duration:

| Command (use a new output file) | Groups | Saved report |
|---|---:|---|
| `python checks/check_pulse_reachability.py --output NEW.json` | 6 | `results/exact_reachability.json` |
| `python checks/check_finite_accuracy.py --output NEW.json` | 7 | `results/finite_fidelity.json` |
| `python checks/check_control_audit.py --output NEW.json` | 5 | `results/calibration_duration.json` |

`control_integrals.py` supplies the shared integration routines and imports `check_finite_accuracy.py` from this directory.

Use `python verify.py --output-dir NEW_DIRECTORY` for complete logs, integrity and comparison records. `test_repository.py` runs eight infrastructure tests of the runner and its records, separately from the 18 scientific groups. See [VERIFICATION](../VERIFICATION.md) for the fixed comparison policy.

The [claim map](../research/MODEL_AND_CLAIMS.md) links each result to its analytic proof and supporting suite.
