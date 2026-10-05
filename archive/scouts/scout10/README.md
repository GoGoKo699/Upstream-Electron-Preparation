# Scout 10: fixed one-input electron-preparation candidate

**5 October 2026. Decision: GO for focused theoretical development, not a priority or PRL-acceptance certificate.** No repository, manuscript, device proposal or outside invitation was created. Earlier unrelated spin-offs remain outside the scope.

Read `SCOUT_10.md` for the claim-level predecessor comparison and two new properties of the existing optimizer. The primary result remains the finite-energy full-many-body-fidelity frontier in `prior/SCOUT_09.md`. The new calculation does not change the Hamiltonian or target, add an actuator, or substitute voltage error for state fidelity.

## New assessment

The 2011 restoration proposal explicitly applies a voltage after the interaction. It is not contradicted by a bound on a restricted upstream source. The 2021 quantum-signal paper is now read from its full publisher PDF; its excitation decomposition and specific entropy-based source optimization do not supply the inspected arbitrary-waveform energy-constrained frontier. The 1997 pulse variational problem has a different noise/charge objective. The 2018 decoherence paper remains abstract-only because full-text routes failed.

For the nominal equal-splitting energy optimizer, deterministic splitting error epsilon changes the actual logarithmic infidelity by **exactly epsilon^2 K_mu**. Its required calibration for a fixed fractional penalty scales with the nominal infidelity. Its RMS source-energy duration grows inversely with the nominal infidelity at fixed target width. These statements describe that optimizer, not a universal robustness or minimum-time bound over all possible controls.

## Reproduce

Use Python with NumPy, SciPy and SymPy as recorded in environment.json. Run with fresh output files:

    python check_control_audit.py --output NEW_CONTROL.json
    python prior/check_finite_accuracy.py --output NEW_ACCURACY.json
    python prior/prior/check_pulse_reachability.py --output NEW_REACHABILITY.json

The new five groups passed on the first run, after the helper-module rename, and on repetition. Their JSON outputs match exactly. The prior seven and six groups were rerun unchanged and reproduced their stored JSON bytes. All 39 original manifest entries remain unchanged. No new scientific test failed or tolerance was relaxed. Log runtimes/terminal notices are not claimed byte-identical.

`control_integrals.py` supplies the tested scalar quadratures. The original exploratory version and first checker import are preserved under `development/`; the rename changes organization, not an equation. The helper includes analytic omitted-frequency tail bounds, while QUADPACK and finite-precision errors remain diagnostic estimates rather than interval certificates. The scalar quadrature refinements and independent direct-coordinate checks are in `evidence/`.

`SOURCES.json` records exact reading depth and failures. No third-party PDF or font is redistributed. `RUN_RECORD.json` pins the completed checks. The delivered archive manifest hashes every member except itself. No downstream-actuator variant, general robust optimizer, finite-duration theorem, mixed-temperature fidelity or achieved laboratory precision is claimed.

A dedicated repository is appropriate only after a new destination is explicitly authorized. Further work should organize and critically assess this fixed claim rather than append another pulse sweep or a new channel.
