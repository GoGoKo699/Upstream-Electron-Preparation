# Physical-premise support and mismatch audit

**5 October 2026. Bounded author-side audit complete; conditional wording retained.**

Base: `04b83e78b6c39125497fc940cc3c566757ced72a`, tree
`59ec3abc17bdbcd1dc9aea32cb9cc274c611b59c`. This record checks the three
inherited premises used together by the [manuscript plan](../research/MANUSCRIPT_PLAN.md).
It adds no theorem, numerical campaign or independent scientific certification.
Source keys and actual reading depths are in [PRIOR_ART](PRIOR_ART.md).

## 1. Decision

Retain C1–C2 as an **exact ideal preparation-feasibility benchmark**. The
sources support its formal ingredients and experimental manifestations of some
of them. They do not establish a device operating regime satisfying all the
assumptions together. No formula, coefficient or proof dependency needs changing
on the evidence inspected. Clarify one accounting term: the budget is excess
energy launched into the driven incoming edge, including its eventual partition
between both outputs. It is not the full electrical work of the bias circuit.

The five-to-ten relevant-precedent benchmark remains **incomplete**. This
bounded support/mismatch record is complete; the broader evidence obligation is
not. Substantial impact, exhaustive priority and independent review remain open.

## 2. Direct formal support

| Premise used by C1–C2 | Inspected support | Scope of that support |
|---|---|---|
| P1: two open channels with a unitary two-mode transfer; after a common delay, $H_p(\omega)=p+(1-p)e^{i\omega\tau}$ | G13 Eqs. (19)–(22); retained C18 Eqs. (16)–(17); DG10 Eqs. (3)–(4) | G13 gives the short-range dispersionless model directly. DG10 derives an effective transfer using low-frequency/locality assumptions. Extending the ideal expression over the optimization's whole frequency axis is a model assumption. |
| P2: a deterministic voltage on a zero-temperature sea gives coherent displacements, whose outputs factorize under linear elastic scattering; the prescribed Lorentzian gives one clean electron | G13 Eq. (20), Section III.A.2 and Appendix C; retained C18 Section III.A and charge conventions; K06 Eqs. (2)–(8) | Coupled-output purity and the clean target are distinct inherited facts. K06 alone does not prove the former. G13's periodic shifted-sea convention alone does not prove our isolated equal-charge infrared limit. |
| P3: the injected-edge excess energy is quadratic in voltage and is redistributed between the two outputs | G13 Eq. (20) and unitary scattering; DG10 Eqs. (3), (5)–(6); B14 paragraph after Eq. (20) and Eqs. (22)–(23) | B14 supplies an arbitrary periodic-bias contact normalization and separates energy, heat and source power. The whole-line functional and output partition follow from the coherent amplitude and unitarity as below. |

G13 Appendix C uses displaced thermal mixtures at finite temperature; it does
not license a pure-state extension. I97 supplies minimal-noise pulse history,
not an additional proof of coupled-channel coherent-product outputs. The
existing [frontier audit](../research/FRONTIER_AUDIT.md) remains necessary:
equal charge and finite energy do not alone ensure finite relative displacement
norm. Its zero-fidelity infrared limit and finite-norm optimizers are unchanged.

## 3. Experimental ingredients and mismatches

| Source | Relevant ingredient | Why it does not certify the complete preparation task |
|---|---|---|
| B13 | Frequency-resolved charge and neutral modes, with mixing consistent with approximately equal weights | Its measured band requires dispersion and dissipation beyond the zero-range ideal description. Approximate mixing is not exact equal splitting across the optimized spectrum. |
| F15 | The equal-weight transfer is used to interpret an HOM fractionalization experiment. Its fully open source is voltage-equivalent; the written zero-temperature coherent outputs factorize. | Periodic electron/hole emissions and HOM signals are not the optimized isolated charge-one waveform or its full target-state fidelity. The different partially open source must not be assigned the same purity argument. |
| H17 | Time-resolved co-propagating density modes | The experiment reports asymmetry and attenuation, with finite-temperature charge packets. Its mixing-angle convention differs from G13's; neither equality nor pure-electron preparation follows. |
| D13 | Voltage-generated Lorentzian source and noise/spectroscopy measurements | Finite electronic temperature and the stated excess-noise interpretation limit do not establish zero-temperature global fidelity after our fixed interacting channel. Main-body reading remains incomplete. |
| LS10 | Energy exchange between channels without charge exchange | Its nonequilibrium QPC source differs from our coherent drive. The discrepancy with the two-channel energy prediction motivates additional degrees of freedom in that setting; it is not a counterexample to our conditional theorem. |

F15 is a particularly close ingredient-level precedent, but no source here
demonstrates the jointly required exact transfer, zero-temperature state,
arbitrary optimized tails and amplitudes, and full selected-state objective.
There is no demonstrated operating window uniform as $\mathcal F\uparrow1$.
No sample parameter, achieved fidelity or universal leakage percentage is
imported. C18's previously recorded implementation limits remain relevant.

## 4. Energy convention and accounting check

The following is our bookkeeping derivation from the inherited amplitude, not
a new experimental result. With the repository Fourier convention, G13 gives

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
$\sum_j|S_{j1}(\omega)|^2=1$, hence
$\mathcal E_{\rm selected}+\mathcal E_{\rm unused}=\mathcal E_{\rm in}$.
All energies are excess energies relative to the common equilibrium reference.

B14's unit-transmission periodic result has the same contact normalization.
Its reservoir heat and full electrical source power are different accounts;
its two-terminal work partition must not be promoted into a universal circuit
factor. The theorem budgets launched edge energy, not waveform-generator or
cryostat consumption. This clarification changes no frontier equation, target
energy $\mathcal E_\ell=\hbar/(2w)$, reference report or output-allocation limit.

## 5. Wording, remaining evidence and stop

The plan can retain necessity and attainability **within its stated model**.
Extra waveform restrictions under the same dynamics, energy and objective
preserve the ideal minimum as a lower bound and may remove attainment.
Dispersion, dissipation, additional modes or a thermal target change that
problem; the current bound is not automatically a bound for those replacements.

The relevant source pools are explicit: P1 has G13/C18/DG10 formal support and
F15 model use, with B13/H17 documenting ingredients and mismatches; P2 has
G13/C18/F15 coherent-output treatment, K06 target construction and D13 source
evidence; P3 has G13/DG10/B14 accounting support and LS10's apparatus warning.
These overlapping pools are not five-to-ten independent, fully model-matched
precedents per convention. Generic citations, unread bibliographies and repeated
counting of one source cannot close that obligation.

Further evidence must address a named gap, especially a justified joint regime,
or materially change the significance/priority assessment. The present audit
finds no concrete blocker to conditional C1–C2, but does not establish practical
advantage or substantial impact. **Stop after repository integration.** No
manuscript prose, additional model, external contact or numerical campaign is
initiated; the [work order](../work_orders/CURRENT.md) preserves that boundary.
