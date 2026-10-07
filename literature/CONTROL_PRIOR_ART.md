# Closest control precedents and the remaining contribution

Correction, prescribed-current synthesis, experimental precompensation and
two-input protection are established control ideas. This comparison identifies
their objectives and control access, then locates the fixed preparation problem
studied here. Reading depths and bibliographic links are in [PRIOR_ART](PRIOR_ART.md).

| Source and inspected passage | Established control or objective | Distinction from C1–C2 |
|---|---|---|
| L11, Eqs. (4), (6)–(7), text after Eq. (11) | Downstream voltage maximizes full many-body restoration overlap in a single-edge all-pass model. | Full-state correction is prior. The fixed open selected port, its transmission zeros and the upstream injected-energy constraint define a different task. |
| M18, Sections II and III.B, Eqs. (22)–(27) | Harmonic engineering produces a prescribed current through a screened gate response; the model excludes inter-edge coupling. | Frequency-response inversion and pulse shaping are prior. The transfer, periodic gate actuator and current/noise objective differ. |
| B19, single-Lorentzian subsection and Methods A–B, author pp. 9 and 13–14 | Calibrated upstream harmonics compensate Coulomb-induced phase/amplitude changes to reconstruct a Lorentzian current at the splitter. | Interaction precompensation is prior. The inspected experiment uses a periodic finite-harmonic source, finite temperature and single-particle tomography; its Lorentzian data are at filling factor three. It does not establish our isolated two-channel full-state energy frontier. |
| R20, Section V, Eqs. (40)–(42) | Proportional drives on both channels excite a scattering eigenmode and remove fractionalization effects from the HOM signal. | Two-input protection is prior. Its eigenmode construction is not the minimum combined energy for a specified selected-output many-body overlap. Our [matched-fidelity comparison](../research/CONTROL_COMPARISON.md) is a supporting corollary, not a new control principle. |
| R21, Sections IV.B and V.A.1–2, Eqs. (43)–(45) | Source parameters are optimized using electron–hole entropy. | Many-body source-quality optimization is prior. The inspected finite-parameter objective does not supply the arbitrary-waveform energy–target-fidelity law. |
| G13/C18; construction audit | Coherent voltage propagation, pure distorted outputs, clean fractionalization inputs and, in C18, protection by changed geometry. | The dynamics and state description are inherited. The closed-inner-channel transfer is not our fixed open channel. |

## The fixed preparation problem

C1–C2 give the complete preparation law for **one driven upstream port,
fixed open-channel transfer, one prescribed electron and its sea, and a total
launched-edge energy budget**. It includes the lower bound over all admitted
real charge-one $`L^1\cap L^2`$ waveforms, an admissible attaining pulse at every
positive error, and the explicit fixed-width singular endpoint.

Quadratic completion is standard. The inverse-infidelity exponent reflects
simple transfer zeros and is not a new general principle or a uniquely
fermionic exponent. The physical contribution rests on specifying the complete
state-preparation task and its restricted-control cost. The comparisons above
are limited to the identified passages and distinguish their control resources
and objectives from this preparation law.

The [same-fidelity control comparison](../research/CONTROL_COMPARISON.md)
shows that the interpretation survives assigning both control classes the same
target and error. The two-input construction is attributed to the established
control idea; the corollary quantifies its cost for the stated target fidelity.

## Reading scope

B19's source/observable setup, Lorentzian subsection and Methods A–B were
inspected in its author PDF. M18's model, current-response equations and noise
definitions, and R20's model and two-input section, were checked at the depths
listed in the [reading ledger](PRIOR_ART.md). These are construction-level
comparisons, rather than reproductions of those papers' full algorithms,
appendices or data.

The source selection follows precompensation, prescribed-current synthesis,
voltage/fidelity/energy optimization and directly relevant references. The
comparison is anchored to the exact target, dynamics, objective and control
class in the [claim map](../research/MODEL_AND_CLAIMS.md).
