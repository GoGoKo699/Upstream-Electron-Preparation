# Claim-driven manuscript plan

**5 October 2026. Planning complete; no manuscript drafted.**

Base: `8506b6a7bd571be98c585259782ea882e00fcbda`, tree
`0912045f6322c642ab47f92b8bd328e9888647cc`. This plan implements the bounded
GO in [SIGNIFICANCE](SIGNIFICANCE.md). It selects the argument and records its
dependencies; it adds no theorem, numerical campaign or claim of independent
review.

## 1. The question the paper must answer

For a prescribed outgoing Lorentzian electron and its Fermi sea, what source
energy is sufficient and necessary when only one upstream contact can be driven
through a fixed lossless two-channel interaction?

The intended contribution is an **exact ideal feasibility benchmark**. Fix the
transfer parameters, target width and positive allowed error. A source budget
below the frontier cannot be rescued by choosing another pulse family: the
competitors already include negative voltage, incoming holes and arbitrarily
long predetermined tails. A budget at or above it permits preparation in the
declared ideal class through the explicit optimum.

This answers the finite-error preparation question left open by a singular
exact inverse. It establishes a conditional reference for pulse design. It does
not yet establish how consequential that reference is for a particular device
or for the wider field; that is the remaining significance question.

## 2. Fixed specification and central claims

Use the [model map](MODEL_AND_CLAIMS.md) without changing its resources: two open
channels; zero-temperature seas; linear, lossless dispersionless collective-mode
scattering; a real deterministic charge-one voltage in $L^1\cap L^2$ at one input;
fixed Lorentzian width $w>0$ and center; an unrestricted unused output. Count
total injected source energy, including energy sent to the other output.
Use full selected-output fidelity, with the common infrared-limit convention
when relative displacement norm diverges. Every optimal pulse has finite norm.

Let $a=2w/\tau$, $R=\mathcal E_{\rm in}/\mathcal E_\ell$ and
$\mathcal E_\ell=\hbar/(2w)$. Define the budget by an inequality, and define

```math
R_{\min}(\mathcal F_0;p,a)
=\min\{R[v]:\mathcal F[v]\ge\mathcal F_0\},
\qquad 0<\mathcal F_0<1.
```

**C1: the complete finite-error frontier.** Use the existing $A_\mu,R_\mu,D_\mu$
from [Frontier, Section 3](FIDELITY_FRONTIER.md#3-exact-optimum-over-arbitrary-allowed-inputs).
Select the unique $\mu>0$ with $D_\mu=-\ln\mathcal F_0$; then
$R_{\min}=R_\mu$. For $R_{\rm cap}>0$, preparation with
$\mathcal F\ge\mathcal F_0$ and $R\le R_{\rm cap}$ is possible in this class
if and only if $R_{\rm cap}\ge R_\mu$. Necessity and attainment both belong
in the central statement. At unequal splitting the budget-parametrized frontier
reaches fidelity one at the finite exact-inverse cost; excess budget can be left
unused. Zero energy is a limit, not an admissible charge-one pulse.

**C2: the equal-splitting endpoint.** At $p=1/2$, exact preparation requires
infinite energy, while every $0<\mathcal F_0<1$ has finite cost. At fixed $a>0$,

```math
R_{\min}(\mathcal F_0;1/2,a)
\sim\frac{C(a)}{-\ln\mathcal F_0}
\sim\frac{C(a)}{1-\mathcal F_0},\qquad\mathcal F_0\uparrow1,
```

with the existing explicit positive coefficient in Frontier, Section 4.
Use the full frontier for finite-error comparisons. Do not use this asymptote
as a width-uniform law or claim a discontinuity at fixed nonzero error.

## 3. Claim, assumption and evidence map

The proof passages are the logical evidence. Existing test groups provide
normalization, algebraic and numerical checks; their counts are not proofs.

| Intended statement | Necessary ingredients | Exact proof route | Existing supporting checks |
|---|---|---|---|
| Inherited full-state objective | Coherent voltage-source outputs; equal charge; neutral relative displacement; correct infrared limit | Frontier Sections 1–2, Eqs. (1)–(2); [Audit](FRONTIER_AUDIT.md), Section 1 | Finite-fidelity: overlap normalization/charge and regulated fermionic determinant checks |
| C1: lower bound over every allowed waveform | Same target, transfer, total-source budget and deterministic input class; nonnegative quadratic completion | Frontier Section 3, Eqs. (3)–(5); Audit Section 3, including infinite-$D$ competitors | Finite-fidelity: global completion/monotonicity and independent frequency quadrature |
| C1: attainment and coverage | Hermitian spectrum; $L^1\cap L^2$ inverse, charge one and finite $D$; monotonic multiplier limits | Audit Sections 2–3 | Normalization and monotonicity checks support the analytic existence argument; they do not test arbitrary tails |
| C2: fixed-width singular endpoint | Equal splitting; nonzero Lorentzian spectrum at transfer zeros; summable full-axis asymptotic bounds | [Reachability](EXACT_REACHABILITY.md), Section 3; Frontier Section 4; Audit Section 4 | Reachability: one-port zero; finite-fidelity: high-fidelity/width dependence and finite-error continuity |
| Interpretation: access to both inputs removes the obstruction | Same unitary matrix, an additional independently driven contact; outputs fixed to target and sea | Reachability Section 6 | Reachability: two-input recovery and energy check |
| Interpretation: optimal energy flows to the unused output | Existing optimizer and unitarity; dominated convergence applied to its selected spectrum | Frontier Section 6, output-energy calculation | Existing energy-conservation check supports accounting; the new explicit limit has an analytic proof, not a separately counted test |

## 4. What changes in understanding or design

| Decision or interpretation | Warranted consequence | Boundary |
|---|---|---|
| Continue searching for a better pulse at a fixed budget? | The exact frontier rules out all permitted waveforms below the necessary cost and supplies an ideal optimum at it. | The fidelity requirement concerns the whole selected state, not an HOM contrast or an early detector gate. |
| Increase energy, relax the target/error, or change control access? | The one-input law separates what pulse shaping can do from changing the task. Two driven inputs can prepare the exact target at combined energy $\mathcal E_\ell$. | The theorem does not rank contact hardware, calibration effort or practical implementation costs. Broadening the electron changes the target. |
| Does an almost correct selected output imply modest source energy? | Along $A_\mu$, $R_{\rm sel}\le1$ and $R_{\rm sel}\to1$, but at equal splitting $R_{\rm unused}\sim R_\mu\to\infty$. | This follows from the optimizer's spectrum; fidelity convergence alone does not imply energy convergence. It is not a heat-production claim or an allocation law for every waveform. |
| Apply the benchmark to restricted hardware? | Extra waveform restrictions under the same transfer, energy and fidelity definitions cannot lower the minimum and may destroy attainment. | Changed dynamics, thermal states, noise or a different observable need their own analysis. No device operating window or detector certificate is supplied. |

The strongest objection remains that the calculation is ordinary quadratic
regularization at known transmission zeros. Address it through the complete
preparation statement and the two resource comparisons above. Attribute the
transfer and coherent-state metric to their established sources; do not present
the method or exponent as a new general principle. The specific L11/R21/C18
comparisons and actual reading depths remain in [SIGNIFICANCE](SIGNIFICANCE.md)
and [PRIOR_ART](../literature/PRIOR_ART.md). They support the recorded distinction
without establishing exhaustive priority. Additional decimal places would not
settle the significance objection.

## 5. Planned order and exclusions

| Part | Required content and purpose |
|---|---|
| Opening question and specification | State the prescribed-electron task, accessible contact, budget and global fidelity before discussing an inverse or an optimizer. |
| Central result | State C1–C2 together: exact finite-error frontier, attaining pulse, and fixed-width endpoint. Include the coefficient and the equal-splitting qualification. |
| Short proof route | Derive the equal-charge metric, give the nonnegative completion, explain admissibility and the transmission-zero asymptote. Point to the detailed bounds. |
| Physical consequences | Explain the feasibility decision, exact two-input control and optimal output-energy allocation. No apparatus-performance claim. |
| Scope and attribution | Give asymmetry, width and finite-error continuity boundaries; attribute inherited ingredients and state unresolved premise/priority evidence. |
| Detailed proof material | Retain infrared qualification, waveform tail/charge estimates and complete-axis asymptotic domination. These are necessary support, not redundant detail. |

Omit C3 from this planned argument: neither the central theorem nor the energy
interpretation needs its separately unaudited occupied-space hole inequality.
Keep it in the repository without promoting its status. Retain the general
finite-target/parity classification as supporting repository material; use only
the one-electron obstruction and asymmetric inverse here. C5 supplies concise
warnings about the nominal optimum's tails and calibration, not a second
optimization claim. No new figure or numerical campaign is required. If a
finite-error example is later useful, use an existing frontier table with its
fixed target ratio and limits explicit.

## 6. Blockers, evidence limits and stopping point

| Open item | Effect on this plan |
|---|---|
| No independent critical report | C1–C2 have an author-side proof/audit, not independent certification. The present review adds no such certification. |
| Incomplete model-matched premise map | Keep the result conditional. The outstanding precedent benchmark in [ASSUMPTIONS](../literature/ASSUMPTIONS.md) is not completed by this plan; no joint apparatus feasibility claim is allowed. |
| Incomplete priority and impact case | Preserve the narrow candidate contribution. A directly covering prior result would change originality; usefulness to a concrete source-design problem remains unestablished. |
| C3's separate proof check | Omission removes it as a dependency of the planned argument. It must be checked before being promoted into a later manuscript. |

No new unresolved mathematical dependency of the conditional C1–C2 statement
was identified in this planning pass. That is an author-side assessment, not a
claim that future criticism cannot find one. The plan supports a compact
conditional theory contribution; a persuasive case for substantial impact
remains open.

**Stop at this plan.** Do not convert it into manuscript prose, add a model or
contact a reviewer automatically. The [work order](../work_orders/CURRENT.md)
records the remaining bounded premise-evidence task for a later continuation.
