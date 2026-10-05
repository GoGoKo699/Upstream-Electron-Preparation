# Scout 09: the finite-energy quantum-state frontier

**5 October 2026.** Continue only the selected single-input electron-fractionalization question from scout 08. No earlier research repository or rejected candidate is reopened.

Read `SCOUT_09.md` for the exact many-body fidelity objective, all-input optimum, charge-sector normalization, high-fidelity energy law and hole-production bound. The optimum uses one deterministic voltage waveform with the original unrestricted whole-line control class. It is not an optimum for arbitrary injected electron sources, randomized protocols, finite-temperature channels, or finite-duration apparatus controls.

**Decision:** the finite-accuracy scientific test passes. The result is an energy–fidelity tradeoff, not a fixed ceiling or a finite-error parity phase. Short fixed target pulses can be costly; broadening the target makes the bound weak, and independently driving both contacts removes the exact obstruction. Precise priority and PRL significance remain open. No new repository, manuscript or external contact is created.

## Reproduce

With Python, NumPy, SciPy and SymPy as recorded in `environment.json`, use new output names:

    OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python check_finite_accuracy.py --output NEW_ACCURACY.json
    OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python prior/check_pulse_reachability.py --output NEW_PRIOR.json

The seven new groups check coherent/fermionic overlap normalization, Slater hole accounting, exact quadratic optimality, independent frequency integration, notch asymptotics, finite-fidelity numerical values and control assumptions. The six prior groups are unchanged. The two final enriched reports agree byte-for-byte, and the prior rerun reproduces the uploaded report exactly.

The numerical frontier is obtained by one-dimensional quadrature with geometric subdivision near transmission minima. Analytic bounds control discarded frequency tails; adaptive quadrature errors are estimates, not interval arithmetic certificates. The all-input theorem follows from completing the square, not a numerical variational search. The largest independent fermionic determinant regulator has dimension 256; it tests the neutral relative phase and does not simulate an entire infinite lead.

The first new script passed assertions but emitted integration warnings with a tangent-coordinate quadrature. The final subdivision removes those warnings without changing formulas or tolerances. The warning-bearing script/log/report and reversible patch are preserved. A subsequent within-group fermionic crosscheck was added; it did not increase the count of test groups. `development/` records both changes. No earlier reference or file is rewritten.

`SOURCES.json` gives actual primary-source reading depth and unsuccessful access. `RUN_RECORD.json` pins the original 12-entry manifest, execution outcomes and report hashes. `MANIFEST.json` in the package verifies its members. No publication PDF, font, linked-account data or unrelated repository is included.

The two `probe_*.py` files are exploratory checks retained for context. They are not additional counted suites, and their earlier integration method is not the final table evaluator.
