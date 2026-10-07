# Precedent coverage for the conditional model

The inherited state and energy premises split into the dependencies used by
C1–C2. This map identifies five relevant primary sources for each convention
and states the exact role of each passage. The [premise audit](PREMISE_AUDIT.md)
records experimental ingredients and model mismatches separately.

## 1. What the counts mean

A counted paper contains a relevant formal construction, explicit use or a
printed model from which the stated translation follows. Each publication
counts once within a row. The same publication can support different premises;
row counts must not be summed as independent confirmations. Shared authors and
theoretical ancestry are substantial. The table classifies the supporting
constructions, model uses and translations; its counts measure source coverage.

| Inherited convention | Five distinct formal precedents | Strength and exact limit |
|---|---|---|
| P1: open local two-channel, lossless two-mode propagation | LS08, DG10, G13, W14, C18 | Three direct scattering constructions and two equivalent rotated Hamiltonians. The translation below is explicit. F15 additionally uses the equal-weight transfer; B13/H17 supply experimental ingredient and mismatch evidence. |
| P2a: deterministic voltage gives coherent displacements and factorized outputs under the stated linear scattering | G13, C18, F15, F14, R20 | Explicit constructions or uses of the coherent scattering argument, including F15's ideal voltage-equivalent source explanation. Neither finite-temperature ket purity nor arbitrary-source purity is inferred. |
| P2b: the quantized Lorentzian supplies the prescribed clean electron plus sea | K06, G13, M15, MH16, F14 | Four source constructions and F14's explicit use. Periodic source papers require their isolated-pulse limit for our whole-line target. D13 supplies additional experimental source evidence. |
| P3a: launched-edge excess energy has coefficient $`e^2/(2h)`$ multiplying the voltage-squared integral | B14, M14, M16, G13, C18 | Three printed voltage/Joule formulas and two exact-amplitude translations via oscillator energy and Parseval. MH17 adds a target-energy cross-check. |
| P3b: integrated input energy equals the sum of the two output excess energies | DG10, G13, C18, F15, LS08 | DG10 explicitly ties energy conservation to unitarity; the others supply the lossless matrix or mode construction. The norm-to-energy implication is our stated translation. LS10's measured mismatch is not counted as positive conservation evidence. |

The controls, fixed target, unused-output freedom and full-state objective
define the optimization task in the [claim map](../research/MODEL_AND_CLAIMS.md).
The table maps the physical premises used by C1–C2.

## 2. Passage map and translations

Bibliographic links and actual reading depths are in [PRIOR_ART](PRIOR_ART.md).
The following locators identify the precise support rather than a generic
electron-optics citation list.

| Source | Passage used for the counted convention |
|---|---|
| LS08 | Section II.C, Eqs. (18)–(24): local screened interaction, normalized mode rotation and free collective propagation. |
| DG10 | Eqs. (3)–(4): unitary scattering and effective two-mode transfer; Eqs. (5)–(6): electronic/bosonic energy currents. |
| G13 | Section II.A.1, Eqs. (1)–(6): clean Lorentzian source; Sections III.A–B, Eqs. (19)–(22): coherent amplitude, product outputs and transfer. Appendix C distinguishes thermal mixtures. |
| W14 | Eqs. (1)–(2) and following rotation/free-mode paragraphs: local coupling and two chiral velocities on an open segment. |
| C18 | Open-channel Eqs. (16)–(17), Section III.A and Appendix A; exact voltage-displacement prefactor after Eq. (A6). Closed-inner-channel protection is excluded from this model count. |
| F15 | Coherent input/output formulas for the fully open source and the Comparison subsection's equal-weight transmitted/reflected amplitudes. |
| F14 | Main pointer-state discussion; Appendix A, Eqs. (A1)–(A2) and following product-output paragraph; explicit clean Leviton input. |
| R20 | Section II, Eqs. (12)–(15): matrix and coherent voltage propagation. Section V's two-input protection is separately attributed in [CONTROL_PRIOR_ART](CONTROL_PRIOR_ART.md). |
| K06 | Eqs. (2)–(8): Lorentzian phase, no-hole construction and specified electron wavefunction; translate voltage polarity. |
| M15 | Sections II.C and III.A–C, especially Eq. (16): Lorentzian envelope and pure-state stream decomposition, with the isolated/overlapping distinction. |
| MH16 | Sections 3.3.1 and 4–4.1, Eqs. (26)–(32): Lorentzian phase, rank-one zero-temperature coherence and finite-temperature mixture. |
| B14 | Paragraph after Eq. (20): transparent-contact voltage-squared normalization; Eqs. (22)–(23): energy, heat and full-power accounts. |
| M14 | Eq. (7) and transparent-leviton example: receiving-branch normalization. Its erratum changes reflected heat noise, not mean Eq. (7). Count the paper and erratum as one precedent. |
| M16 | General zero-temperature voltage-driven Joule law, Eq. (8), together with Eq. (1)'s current normalization. Its half-flux example is not imported into our charge-one task. |
| MH17 (additional) | Eqs. (2)–(3) and (9): Lorentzian target energy and current-energy check. This is distinct from MH16 and is listed separately from the five general entries. |

**Hamiltonian-to-transfer translation.** LS08/W14 give a real orthogonal mode
rotation $`U`$ and free chiral velocities $`u_\pm`$. Propagation across an open
segment of length $`L`$ therefore has

```math
S(\omega,L)=U\operatorname{diag}(e^{i\omega L/u_+},e^{i\omega L/u_-})U^T.
```

Its selected diagonal element has two phase factors weighted by squared mixing
coefficients; removing one common delay gives $`H_p`$. This is our algebraic
translation, not a claim that those papers print the present scalar optimum.
The low-energy/local-interaction approximation remains explicit.

**Amplitude-to-energy translation.** G13 and C18 give
$`\Lambda(\omega)=-e\widehat V(\omega)/(h\sqrt\omega)`$.
The [accounting derivation](PREMISE_AUDIT.md#4-energy-convention-and-accounting-check)
then gives

```math
\mathcal E=\int_0^\infty\hbar\omega|\Lambda|^2d\omega
=\frac{e^2}{2h}\int V^2dt,
```

including the positive-frequency Parseval factor.
Unitarity preserves this frequencywise norm and hence the integrated sum of
both outgoing energies. This is not an assertion of equal instantaneous fluxes
at different cross-sections. Neither circuit reservoir partition nor heat
terminology is substituted for the repository's launched-edge budget.

## 3. Experimental scope

The [support/mismatch table](PREMISE_AUDIT.md#3-experimental-ingredients-and-mismatches)
records the source-specific comparisons. B13 and H17 resolve modes with departures
from the ideal limit;
F15 supplies close model use; D13 tests source ingredients at finite temperature;
LS10 warns against assuming only two lossless energy-carrying modes in every
apparatus. B19 establishes calibrated precompensation in a different periodic
setting.

Exact zero temperature and an unlimited ideal waveform class are premises of
the mathematical optimization. Relating its frontier to a device requires a
transfer model valid over the optimized spectrum and a justified connection
between the measured observable and the target-state overlap. These requirements
are particularly relevant in the high-fidelity limit.

## 4. Source coverage

Every counted paper is tied to an inspected primary passage. The [reading
ledger](PRIOR_ART.md) states versions and exact depths; the [control
comparison](CONTROL_PRIOR_ART.md) distinguishes the preparation task from
established correction and pulse-shaping constructions.
