# Physical premises and energy accounting

C1–C2 combine a lossless two-mode transfer, a voltage-generated coherent state
and a launched-edge energy budget. This note connects those premises to
primary sources, identifies experimental model mismatches, and derives the
energy convention. Source keys and reading depths are in [PRIOR_ART](PRIOR_ART.md).

## 1. Model and evidence

The [claim map](../research/MODEL_AND_CLAIMS.md) specifies an exact ideal
preparation-feasibility problem. The sources below support its formal
ingredients and experimental manifestations of some of them. The energy
budget counts excess energy launched into the driven incoming edge, including
its eventual partition between both outputs; full electrical work of the bias
circuit is a different quantity.

## 2. Direct formal support

| Premise used by C1–C2 | Inspected support | Scope of that support |
|---|---|---|
| P1: two open channels with a unitary two-mode transfer; after a common delay, $`H_p(\omega)=p+(1-p)e^{i\omega\tau}`$ | G13 Eqs. (19)–(22); C18 Eqs. (16)–(17); DG10 Eqs. (3)–(4) | G13 gives the short-range dispersionless model directly. DG10 derives an effective transfer using low-frequency/locality assumptions. Extending the ideal expression over the optimization's whole frequency axis is a model assumption. |
| P2: a deterministic voltage on a zero-temperature sea gives coherent displacements, whose outputs factorize under linear elastic scattering; the prescribed Lorentzian gives one clean electron | G13 Eq. (20), Section III.A.2 and Appendix C; C18 Section III.A and charge conventions; K06 Eqs. (2)–(8) | Coupled-output purity and the clean target are distinct inherited facts. K06 alone does not prove the former. G13's periodic shifted-sea convention alone does not prove our isolated equal-charge infrared limit. |
| P3: the injected-edge excess energy is quadratic in voltage and is redistributed between the two outputs | G13 Eq. (20) and unitary scattering; DG10 Eqs. (3), (5)–(6); B14 paragraph after Eq. (20) and Eqs. (22)–(23) | B14 supplies an arbitrary periodic-bias contact normalization and separates energy, heat and source power. The whole-line functional and output partition follow from the coherent amplitude and unitarity as below. |

G13 Appendix C uses displaced thermal mixtures at finite temperature; it does
not license a pure-state extension. I97 supplies minimal-noise pulse history,
not an additional proof of coupled-channel coherent-product outputs. The
[frontier audit](../research/FRONTIER_AUDIT.md) remains necessary:
equal charge and finite energy do not alone ensure finite relative displacement
norm. The audit defines the zero-fidelity infrared limit and proves that the optimizers have finite norm.

## 3. Experimental ingredients and mismatches

| Source | Relevant ingredient | Model or observable mismatch |
|---|---|---|
| B13 | Frequency-resolved charge and neutral modes, with mixing consistent with approximately equal weights | Its measured band requires dispersion and dissipation beyond the zero-range ideal description. Approximate mixing is not exact equal splitting across the optimized spectrum. |
| F15 | The equal-weight transfer is used to interpret an HOM fractionalization experiment. Its fully open source is voltage-equivalent; the written zero-temperature coherent outputs factorize. | Periodic electron/hole emissions and HOM signals are not the optimized isolated charge-one waveform or its full target-state fidelity. The different partially open source must not be assigned the same purity argument. |
| H17 | Time-resolved co-propagating density modes | The experiment reports asymmetry and attenuation, with finite-temperature charge packets. Its mixing-angle convention differs from G13's; neither equality nor pure-electron preparation follows. |
| D13 | Voltage-generated Lorentzian source and noise/spectroscopy measurements | Finite electronic temperature and the stated excess-noise interpretation limit do not establish zero-temperature global fidelity after our fixed interacting channel. The ledger records abstract/preview main-paper coverage and the inspected supplementary sections. |
| LS10 | Energy exchange between channels without charge exchange | Its nonequilibrium QPC source differs from our coherent drive. The discrepancy with the two-channel energy prediction motivates additional degrees of freedom in that setting; it is not a counterexample to our conditional theorem. |

F15 supplies particularly close model ingredients. Applying the optimized
isolated-pulse solution to an experiment additionally requires agreement over
the pulse spectrum, a justified temperature regime and control of the required
tails and amplitudes. These requirements become more demanding toward unit
fidelity. C18's isolated-pulse and interaction-model qualifications are also
relevant to that comparison.

## 4. Energy convention and accounting check

With the repository Fourier convention, G13 gives the coherent amplitude

```math
\Lambda(\omega)=-\frac{e\widehat V(\omega)}{h\sqrt\omega}
=-\frac{\widehat v(\omega)}{2\pi\sqrt\omega}.
```

For a real finite-energy drive, the excess bosonic energy and Parseval identity
give

```math
\mathcal E_{\rm in}
=\int_0^\infty\hbar\omega|\Lambda(\omega)|^2d\omega
=\frac{\hbar}{4\pi^2}\int_0^\infty|\widehat v(\omega)|^2d\omega
=\frac{\hbar}{4\pi}\int_{\mathbb R}v(t)^2dt
=\frac{e^2}{2h}\int_{\mathbb R}V(t)^2dt.
```

The energy integral can remain finite despite the charged displacement's
infrared number singularity. For the undriven second input, unitarity gives
$`\sum_j|S_{j1}(\omega)|^2=1`$, hence
$`\mathcal E_{\rm selected}+\mathcal E_{\rm unused}=\mathcal E_{\rm in}`$.
All energies are excess energies relative to the common equilibrium reference.

B14's unit-transmission periodic result has the same contact normalization.
Its reservoir heat and full electrical source power are different accounts;
its two-terminal work partition must not be promoted into a universal circuit
factor. The theorem budgets launched edge energy, not waveform-generator or
cryostat consumption. The target normalization is
$`\mathcal E_\ell=\hbar/(2w)`$.

## 5. Scope under additional restrictions

Necessity and attainability hold within the stated model. Extra waveform
restrictions under the same dynamics, energy and objective preserve the ideal
minimum as a lower bound and may remove attainment. Dispersion, dissipation,
additional modes or a thermal target change that problem; the current bound
is not automatically a bound for those replacements.

## 6. Formal precedent map

The [passage map](PRECEDENT_MAP.md) separates the state and energy premises
into P1, P2a, P2b, P3a and P3b, with five distinct formal primary sources for
each. It identifies printed formulas, explicit model uses and algebraic
translations. Each publication counts once within a row; the overlapping pools
share authors and theoretical ancestry. The [reading ledger](PRIOR_ART.md)
gives versions and exact depths.

C18 gives the exact voltage-displacement prefactor in Appendix A,
immediately after Eq. (A6), in the author-uploaded manuscript, p. 23. Its
pagination differs from the 28-page publisher PDF used in the
[construction comparison](CABART_2018_COMPARISON.md). The prefactor agrees with
G13 and supplies the same Section 4 Parseval translation. M14 Eq. (7) and M16
Eq. (8) also provide printed contact/Joule normalization statements
within their stated models. M14's erratum concerns reflected heat noise and
does not change mean Eq. (7). MH17, distinct from the coherence paper MH16,
provides a separate Lorentzian target-energy cross-check. The distinction
between circuit work and launched-edge energy, and between reservoir contacts
and copropagating outputs, is retained in these translations.

The [control comparison](CONTROL_PRIOR_ART.md) additionally attributes M18's
prescribed-current synthesis, B19's calibrated experimental precompensation and
R20's two-input eigenmode protection. They narrow the contribution to the exact
fixed-control preparation law. B19's periodic finite-harmonic Lorentzian
experiment at filling factor three and finite temperature is not the present
two-channel full-state frontier.
