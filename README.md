# Upstream Electron Preparation

**Energy and fidelity limits for preparing a prescribed electron state through a fixed interacting channel with one upstream voltage source.**

A voltage pulse that is clean at its source need not arrive as the desired electron after propagating through two interacting quantum Hall edge channels. This repository asks how much source energy is needed to prepare one *specified* outgoing Lorentzian electron, including an otherwise unexcited Fermi sea, when only one upstream contact can be driven.

The channel and coherent-state description are inherited from electron quantum optics. The result under study is a constrained state-preparation frontier, not a new fractionalization mechanism, an intrinsic energy cost of every electron, or irreversible decoherence of every voltage-generated state.

The [significance assessment](research/SIGNIFICANCE.md) supports proceeding to a focused manuscript plan around that frontier. Its physical point is the cost of access to only one source: along the optimum, the diverging energy goes into the unused output while the selected output approaches its prescribed electron. This is an author-side planning decision; priority and independent review remain open.

## The fixed result

Write $x=\omega\tau$, $a=2w/\tau>0$, $H_p(x)=p+(1-p)e^{ix}$, and $A(x)=\widehat v(x/\tau)/(2\pi)$, where $v=eV/\hbar$. With one real, deterministic, integrable finite-energy drive of charge one,

```math
D[A]=-\ln\mathcal F[A]=\int_0^\infty\frac{|H_p(x)A(x)-e^{-ax/2}|^2}{x}\,dx,
\qquad R[A]=\frac{\mathcal E_{\rm in}}{\mathcal E_\ell}=a\int_0^\infty|A(x)|^2dx.
```

Here fidelity means the ordinary squared state overlap when the relative displacement norm is finite, and its common-infrared-regulator limit otherwise. Finite source energy and charge one alone need not give finite $D$; divergent cases have zero limiting fidelity. Every optimizer below has finite $D$. The [critical audit](research/FRONTIER_AUDIT.md) supplies this qualification and the complete proof bounds.

The author-side optimizer is explicit:

```math
A_\mu(x)=\frac{H_p(x)^*e^{-ax/2}}{|H_p(x)|^2+\mu x},\qquad\mu>0.
```

At equal splitting, a perfect single-electron target has no finite-energy inverse. Every fidelity strictly below one is attainable in the ideal input class, and at fixed $a$,

```math
R_{\min}(\mathcal F;a)\sim\frac{C(a)}{-\ln\mathcal F},\qquad
C(a)=a\left[\pi\sum_{k\ge0}\frac{e^{-a(2k+1)\pi}}{\sqrt{(2k+1)\pi}}\right]^2.
```

The full many-body fidelity also bounds unwanted hole content. Exact reachability and the nominal optimizer's duration/calibration sensitivity are supporting results, not alternative global optima. The proof and normalization are in [Fidelity frontier](research/FIDELITY_FRONTIER.md).

## Read in this order

| Document | Purpose |
|---|---|
| [Model and claim map](research/MODEL_AND_CLAIMS.md) | The observable, allowed controls, result hierarchy and proof dependencies. |
| [Fidelity frontier](research/FIDELITY_FRONTIER.md) | Equal-charge overlap, all-waveform optimality, existence, asymptote and hole bound. |
| [Exact reachability](research/EXACT_REACHABILITY.md) | Finite-target classification, asymmetric inverse and control counterexamples. |
| [Optimizer limitations](research/OPTIMIZER_LIMITATIONS.md) | Duration and sensitivity of the same nominal optimum, with finite values. |
| [Prior-art ledger](literature/PRIOR_ART.md) | Inherited ingredients, control-location comparisons and reading depth. |
| [Cabart comparison](literature/CABART_2018_COMPARISON.md) | Why closing the inner channel changes this optimization problem. |
| [Status](STATUS.md) and [workspace entry](WORKSPACE.md) | Established author-side route, open obligations and the next bounded task. |

## Boundaries that matter

Both the propagation geometry and the accessible control port are fixed. The unused input is an equilibrium sea; the unused output is unrestricted. A second driven input, a downstream correcting contact, or a closed inner-channel geometry changes the problem. The model assumes zero temperature, linear dispersion, elastic lossless bosonic scattering and a prescribed coherent voltage. Arbitrarily long tails of either sign are allowed. No finite-start, bandwidth, peak-voltage or repetition-rate constraint is silently imposed.

The objective is the complete selected-output state, not an HOM contrast or a current-profile match. Large costs for a narrow target do not imply the same cost for a broad target. The waveform table is not an achieved apparatus specification. See [Assumptions](literature/ASSUMPTIONS.md).

## Reproduce

Use Python **3.13.5** for the recorded environment. Other environments may reproduce scientific assertions without identical floating-point bytes.

```bash
python -m pip install -r requirements.txt
python verify.py --integrity-only
python checks/test_repository.py
python verify.py --output-dir local-evidence-001
```

The output directory must not already exist. The runner executes the unchanged three scientific suites (**6 + 7 + 5 = 18 groups**), records all logs and field differences, and checks source integrity before and after. Reference bytes are never refreshed automatically. [Verification policy](VERIFICATION.md) distinguishes passing assertions, numerical agreement and exact reproduction. Hosted artifacts identify their own source tree; local success is not a hosted result.

## Status and provenance

This is a theory research workspace. The fixed result has a GO decision for manuscript planning; no manuscript or release has been initiated. The bounded author-side audit of the overlap, admissibility and global optimum is complete, with one infrared-domain clarification and no change to the frontier. Independent validation, exhaustive priority and a complete model-matched physical-premise audit are still absent. The specific Cabart full-text access gap has been closed at the recorded depth, not expanded into a claim of exhaustive review.

[Archive](archive/README.md) preserves the supplied scouts 08–10, development attempts and pre-import readiness record without editing their historical decisions. [Import manifest](provenance/IMPORT_MANIFEST.json) pins every protected copy. No unrelated scientific project or publisher PDF is imported.

The repository retains the owner's existing [MIT license](LICENSE).
