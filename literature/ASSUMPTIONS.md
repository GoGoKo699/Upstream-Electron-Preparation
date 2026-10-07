# Physical assumptions

The result is an exact energy–fidelity frontier within the model below.
The [premise audit](PREMISE_AUDIT.md) explains its physical ingredients and
energy accounting; the [precedent map](PRECEDENT_MAP.md) identifies the primary
passages supporting each inherited convention.

| Assumption in the fixed theorem | Formal support | Physical scope |
|---|---|---|
| Two open copropagating channels, linear electronic dispersion and linear screening (P1) | LS08/DG10/G13/W14/C18: five formal sources, including two Hamiltonian-to-transfer translations. F15 uses the equal-weight transfer; B13/H17 observe mode ingredients and deviations. | The ideal transfer is stipulated over the optimized pulse spectrum. B13/H17 identify dispersion, attenuation and mixing deviations relevant to device modeling. |
| Zero-temperature sea and coherent deterministic voltage input with factorized outputs (P2a) | G13/C18/F15/F14/R20: five coherent-scattering constructions or explicit uses. | This purity argument applies to the stated zero-temperature voltage source. Thermal inputs are mixtures; generic electronic sources can entangle the outputs. |
| Prescribed clean Lorentzian electron and its sea (P2b) | K06/G13/M15/MH16 construct the source; F14 explicitly uses it. D13 supplies additional source measurements with temperature/observable qualifications. | The target is an isolated pulse; periodic constructions require their separated-pulse limit. |
| Only one upstream contact is driven; geometry remains fixed | Explicit mathematical control class. [Control precedents](CONTROL_PRIOR_ART.md) distinguish L11 downstream correction, C18 loop geometry, M18 gate shaping, B19 calibrated precompensation and R20 two-input protection. | Other actuators, feedback or changed geometry define different preparation tasks. |
| Arbitrary real $`L^1\cap L^2`$ charge-one waveform, both signs, long tails | Constructive admissibility proof in [FIDELITY_FRONTIER](../research/FIDELITY_FRONTIER.md). | Finite start, bandwidth, amplitude and repetition constraints can restrict this ideal waveform class. |
| Full selected-output many-body fidelity | Equal-charge Weyl displacement and single-electron/fermionic regulator checks. The [audit](../research/FRONTIER_AUDIT.md) distinguishes finite-norm ket overlap from the zero-fidelity infrared limit. | This is the overlap with the electron and its entire sea. HOM overlap measures a different quantity. |
| Injected-edge excess energy has the voltage-squared coefficient (P3a) | B14/M14/M16 printed voltage/Joule formulas and G13/C18 exact-amplitude translations: five general formal precedents. MH17 separately checks the Lorentzian target energy. | The budget counts energy launched into the edge; full bias-circuit work uses a different accounting convention. |
| Injected energy equals the sum of both output excess energies (P3b) | DG10/G13/C18/F15/LS08 supply energy-conserving scattering or the lossless mode model; the frequency-norm-to-integrated-energy translation is explicit in the premise audit. | This is integrated energy conservation. LS10 identifies additional-energy-mode concerns in a different source setting; instantaneous fluxes can differ between cross-sections. |

The [coverage map](PRECEDENT_MAP.md) contains five distinct formal primary
precedents per stated subpremise. Each publication counts once within a row;
shared authors and theoretical ancestry make these overlapping source pools.
The source-derived experimental ingredients and their specific model mismatches
are recorded separately in the [premise audit](PREMISE_AUDIT.md#3-experimental-ingredients-and-mismatches).

The [claim map](../research/MODEL_AND_CLAIMS.md) fixes the target, controls and
proof dependencies. Extra waveform restrictions preserve the ideal lower bound
when the dynamics, energy and fidelity remain the same, although attainment
can be lost. Changed dynamics or a thermal target require a new analysis.
C18's isolated-pulse discussion also explains why long preparation tails need
care when comparing with periodically operated sources.

Source keys and exact reading depths are in [PRIOR_ART](PRIOR_ART.md).
