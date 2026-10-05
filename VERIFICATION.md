# Verification and comparison policy

## Commands and outputs

`python verify.py --integrity-only` checks the 83 imported file copies, the existing license, active local links and excluded publication/font/bytecode extensions. `python checks/test_repository.py` runs eight infrastructure tests. `python verify.py --output-dir NEW_DIRECTORY` executes all three unchanged scientific suites and stores their complete logs, observed and reference reports, comparisons, environment, before/after integrity, exact source hashes and tracked-source ZIP.

The total remains **18 scientific groups**. The eight runner/infrastructure tests are separate. No claimed theorem is established by test counts. The full run requires a fresh output directory and does not update anything under results/ or archive/. A failure does not authorize changing an original assertion or reference.

## Four separate questions

1. Did each original suite exit successfully and report its expected number of passing groups?
2. Did it numerically agree with its canonical original report under this comparison policy?
3. Were the observed JSON bytes identical to the reference bytes?
4. Did the exact checked source and every imported file remain unchanged during execution?

The machine report answers each separately. A successful numerical comparison is not byte reproduction. Neither is independent scientific review.

## Fixed numerical policy

JSON dictionary keys, list lengths, value types, integers, booleans and strings must agree exactly. Floats must be finite; all changed float values are recorded, including accepted changes. Numerical comparison uses relative tolerance **1e-9** and absolute tolerance **5e-10**, applying the standard `abs(a-b) <= max(rtol*max(abs(a),abs(b)), atol)` criterion. The original scientific tests retain their own unchanged assertions and tolerances; this policy is an additional cross-environment reproduction check, not a replacement for those assertions.

No workload-counter override or special source-scoped waiver is imported from another project. No raw difference is hidden. A changed quadrature error estimate is still reported as a changed field; these estimates are diagnostics rather than physical observables or interval-certified bounds. If a future hosted run exceeds the policy, inspect its precise differences and underlying suite assertions before proposing a documented change. Do not refresh the reference.

## Source and hosted evidence

The incoming base is recorded in provenance/IMPORT_MANIFEST.json. Scientific source files are mapped to the original scout member and SHA-256. Original archives are byte-preserved as extracted members; their original ZIP byte hashes are recorded separately. The repository's MIT license was already supplied by the owner.

Continuous integration runs on the head revision, records the actual commit/tree in REPORT.json and tracked-source.zip, and uploads evidence even if a check fails. It uses read-only content permissions. Inspect both the pull-request and merged-main runs: one does not prove the other. A downloaded artifact's source hashes should match the intended complete tree before its numerical report is used.

The pre-import local run is preserved in IMPORT_RECORD.json. Fresh candidate and hosted results belong to their own artifacts and PR handoff; none is fabricated prospectively in that record. No ongoing monitoring or scheduled external delivery is part of initialization.
