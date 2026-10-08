# Scope and evidence

The repository develops an energy–fidelity frontier for preparing a prescribed
Lorentzian electron and its Fermi sea through two interacting quantum Hall edge
channels. One upstream voltage is controlled; the target width and center,
channel dynamics and full-state fidelity are fixed.

## Results and proof route

| Result | Read |
|---|---|
| Exact minimum source energy at prescribed fidelity, attained by an explicit waveform | [Fidelity frontier](research/FIDELITY_FRONTIER.md), Sections 2–4 |
| Inverse-error energy divergence at equal splitting and fixed target width | [Frontier](research/FIDELITY_FRONTIER.md), Section 4, and [whole-axis proof](research/FRONTIER_AUDIT.md#4-a-bound-over-the-entire-frequency-axis) |
| Lower energy with two controlled inputs at the same target and fidelity | [Control comparison](research/CONTROL_COMPARISON.md) |

The [model and claim map](research/MODEL_AND_CLAIMS.md) defines the input class,
infrared convention and dependencies. General clean-target
[reachability](research/EXACT_REACHABILITY.md) and the nominal optimizer's
[duration and calibration sensitivity](research/OPTIMIZER_LIMITATIONS.md)
provide supporting results.

## Physical scope

The theory uses zero-temperature, linear, elastic, lossless and dispersionless
bosonic scattering in two open channels. The input is a deterministic real
charge-one voltage with integrable, finite-energy tails. The unused output is
unrestricted, and its energy is included in the launched-edge budget.

The [assumptions](literature/ASSUMPTIONS.md) and
[premise comparison](literature/PREMISE_AUDIT.md) connect this ideal model to
the primary literature. The [control comparison](literature/CONTROL_PRIOR_ART.md)
identifies which earlier constructions use different controls or observables.

## Evidence and reproduction

The analytic proof is supported by **18 scientific groups in three suites**,
with **eight separate infrastructure tests**. The [verification policy](VERIFICATION.md)
defines the checks and distinguishes passing assertions, numerical agreement
and exact-byte reproduction. Each verification artifact records its own commit,
source hashes, raw reports and comparisons.

For learning, start with the [tutorial guide](tutorial/README.md) and
[bridge](tutorial/BRIDGE.md).
