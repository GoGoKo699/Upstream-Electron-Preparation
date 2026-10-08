# Verification and comparison policy

## Commands and outputs

`python verify.py --integrity-only` checks the 83 protected files, the license, active local links and excluded publication/font/bytecode extensions. `python checks/test_repository.py` runs eight infrastructure tests. `python verify.py --output-dir NEW_DIRECTORY` executes all three scientific suites and stores their complete logs, observed and reference reports, comparisons, environment, before/after integrity, exact source hashes and tracked-source ZIP.

The scientific suites contain **18 groups**; the eight infrastructure tests exercise the runner and its records. The [claim map](research/MODEL_AND_CLAIMS.md) links the analytic proofs and their supporting checks. Each full run uses a fresh output directory and preserves the assertions and immutable references under results/ and archive/.

## Report contents

1. Suite exit status and expected passing-group counts.
2. Numerical agreement with the canonical report under the comparison policy.
3. Byte-for-byte agreement between observed and reference JSON.
4. Source and protected-file integrity before and after execution.

The machine report records these separately so that numerical agreement and byte reproduction remain distinguishable.

## Fixed numerical policy

JSON dictionary keys, list lengths, value types, integers, booleans and strings must agree exactly. Floats must be finite; all changed float values are recorded, including accepted changes. Numerical comparison uses relative tolerance **1e-9** and absolute tolerance **5e-10**, applying the standard `abs(a-b) <= max(rtol*max(abs(a),abs(b)), atol)` criterion. The original scientific tests retain their own unchanged assertions and tolerances; this policy is an additional cross-environment reproduction check, not a replacement for those assertions.

Every changed field is reported, including quadrature error estimates. These estimates are diagnostics rather than physical observables or interval-certified bounds. A result outside the policy requires inspection of its precise differences and underlying suite assertions; the reference remains fixed.

## Source and hosted evidence

`provenance/IMPORT_MANIFEST.json` records the protected source files, canonical reports and their SHA-256 hashes.

Continuous integration runs on the head revision, records the actual commit/tree in REPORT.json and tracked-source.zip, and uploads evidence even if a check fails. It uses read-only content permissions. Pull-request and merged-main revisions each receive a separate run. Match a downloaded artifact's source hashes to the intended complete tree before using its numerical report.
