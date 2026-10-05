# Scientific readiness change record

**5 October 2026.** Base `125eb6e576f86aa985b19df955f6f7801adb83b3`, tree
`d480f1ea7841b487b9eae2c1be8ff8aa7837c0d5`.

## Scope correction

The prior active Frontier Section 6 listed finite-temperature, nonlinear-band,
dispersive-mode and calibration models together with waveform restrictions,
then asserted that such restrictions could only worsen the ideal optimum.
That sentence overextended set-inclusion monotonicity to changed dynamics and
state definitions. The corresponding precise boundary was already present in
MODEL_AND_CLAIMS and PREMISE_AUDIT.

The corrected statement limits the lower-bound inheritance to restrictions on
waveforms with the same dynamics, energy and fidelity. Changed dynamics or
thermal states require their own analysis. This removes an unsupported scope
claim; it changes no C1–C2 equation, coefficient, admissible waveform or reference
result. The old statement remains recoverable at the base revision and in the
protected historical import.

## Supporting result and attribution

[CONTROL_COMPARISON](../research/CONTROL_COMPARISON.md) makes the two-input
comparison at equal target fidelity explicit. It reduces to the existing
$H=1$ case of C1 by unitarity, proves admissibility and strict improvement for
interior mixing, and recovers the endpoint contrast. It is a new explicit
supporting derivation, not a changed central theorem. Two author-side
mathematical reviews checked the reduction, domain, charges and endpoints;
they are not independent scientific validation. No extra numerical test was
needed for this analytic corollary.

The targeted premise and [control comparisons](../literature/CONTROL_PRIOR_ART.md)
update attribution and evidence status at recorded reading depths. Earlier
audit decisions remain historical records, linked to the current readiness
decision. No general pulse-shaping or two-input-control priority claim is made.

All 83 protected copies, scientific code, three canonical reports, comparison
tolerances and warning-bearing history are unchanged. Candidate, PR and actual
merged-main evidence are recorded separately in the PR handoff.
