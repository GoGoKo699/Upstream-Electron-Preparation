# Upstream Electron Preparation

**Restricted control creates a sharp energy–fidelity limit for preparing one prescribed electron.**

A voltage pulse that is clean at its source need not arrive as the desired electron
after passing through two interacting quantum Hall edge channels. How much source
energy is needed to prepare a specified outgoing Lorentzian electron, including an
otherwise unexcited Fermi sea, when only one upstream contact can be driven?

| Read next | Purpose |
|---|---|
| [Reading guide](tutorial/README.md) · [Bridge to the result](tutorial/BRIDGE.md) | Learn from one external tutorial and the local derivation |
| [Model and claim map](research/MODEL_AND_CLAIMS.md) · [Frontier](research/FIDELITY_FRONTIER.md) · [Proof audit](research/FRONTIER_AUDIT.md) | Follow the fixed task, exact optimum and proof dependencies |
| [Assumptions](literature/ASSUMPTIONS.md) · [Prior-work comparison](literature/CONTROL_PRIOR_ART.md) | Check physical scope, control access and attribution |
| [Verification](#evidence-and-reproduction) | Reproduce the checks and inspect their evidence |
| [LLM guide](llms.txt) | Find relevant questions, search terms and authoritative files |

## Model and preparation task

| Resource | Fixed specification |
|---|---|
| Target | One Lorentzian electron of prescribed width and center, with its zero-temperature Fermi sea |
| Accessible control | One deterministic, real, charge-one upstream voltage; integrable and finite-energy, with either sign and arbitrarily long tails allowed |
| Propagation | Two open, copropagating channels with linear, elastic, lossless and dispersionless bosonic scattering |
| Other channel | The unused input is an equilibrium sea; the unused output is unrestricted |
| Objective and budget | Full selected-output state fidelity; excess energy launched into the driven incoming edge, counting both eventual outputs |

The target fixes the electron's orbital and the rest of the sea together. A matching
current profile or HOM contrast is a different observable. The source budget is not
the full electrical work of the bias circuit or irreversible heat.

Write $`x=\omega\tau`$, $`a=2w/\tau>0`$, $`H_p(x)=p+(1-p)e^{ix}`$, and
$`A(x)=\widehat v(x/\tau)/(2\pi)`$, where $`v=eV/\hbar`$. Here $`w`$ is the
target width, $`\tau>0`$ the difference in mode flight times, and $`0\le p\le1`$
the mixing weight. The energy–error functionals are

```math
\begin{aligned}
D[A]=-\ln\mathcal F[A]
&=\int_0^\infty\frac{|H_p(x)A(x)-e^{-ax/2}|^2}{x}\,dx,\\
R[A]=\frac{\mathcal E_{\rm in}}{\mathcal E_\ell}
&=a\int_0^\infty|A(x)|^2dx,
\qquad \mathcal E_\ell=\frac{\hbar}{2w}.
\end{aligned}
```

Fidelity is the ordinary squared state overlap when the relative displacement norm
is finite, and its common-infrared-regulator limit otherwise. Finite source energy
and charge one alone need not give finite $`D`$; divergent cases have zero limiting
fidelity. Every optimizer below has finite $`D`$. The
[proof audit](research/FRONTIER_AUDIT.md) gives the qualification and complete bounds.

## The attainable frontier

The minimum source energy at a prescribed fidelity is attained by an explicit pulse:

```math
A_\mu(x)=\frac{H_p(x)^*e^{-ax/2}}{|H_p(x)|^2+\mu x},
\qquad \mu>0.
```

Choose $`\mu`$ so that $`D[A_\mu]=-\ln\mathcal F_0`$ for the desired
$`0<\mathcal F_0<1`$. Below the corresponding energy, no allowed pulse can meet
that full-state fidelity; at the frontier, this pulse does.

At equal splitting, perfect preparation has no finite-energy inverse. Every
$`0<\mathcal F_0<1`$ is attainable in the ideal input class, and at fixed $`a`$,

```math
\boxed{
R_{\min}(\mathcal F;a)\sim\frac{C(a)}{-\ln\mathcal F}
\qquad (\mathcal F\uparrow1)
}
```

```math
C(a)=a\left[
\pi\sum_{k\ge0}\frac{e^{-a(2k+1)\pi}}{\sqrt{(2k+1)\pi}}
\right]^2.
```

The [frontier](research/FIDELITY_FRONTIER.md) supplies the exact finite-error
integrals at fixed target width. The [claim map](research/MODEL_AND_CLAIMS.md)
collects this C1–C2 result and its proof dependencies.

## Why lossless propagation can still be costly

The selected output combines two delayed copies of the input. At equal mixing,
their transfer amplitude vanishes at isolated frequencies. Exact inversion near
those zeros would require infinite input energy; an approximate inverse balances
spectral error against its energy cost.

Along the optimal pulse, the selected-output energy stays at most the target
energy and approaches it at high fidelity. At equal splitting, the divergent
energy leaves through the unused output. The restriction is access to one input
of a lossless two-channel device.

Driving both inputs changes that resource. The
[same-fidelity comparison](research/CONTROL_COMPARISON.md) proves a strictly lower
combined-energy minimum for interior mixing at the same target and error.
The [prior-work comparison](literature/CONTROL_PRIOR_ART.md) attributes the
two-contact control principle and relates it to this energy comparison.

## One tutorial, then this result

The selected external learning anchor is:

> G. Fève, J.-M. Berroir and B. Plaçais, **Time dependent electronic transport in chiral edge channels**,
> *Physica E* **76**, 12–27 (2016).
>
> [Free author-hosted article](https://www.phys.ens.psl.eu/~placais/publication/2016_physicaE_Buttiker-in-memoriam_Feve.pdf) ·
> [Original published article](https://doi.org/10.1016/j.physe.2015.10.006)

The [reading guide](tutorial/README.md) maps its sections. The original
[bridge](tutorial/BRIDGE.md) supplies the clean Lorentzian target, notation,
charge-aware overlap, launched-energy normalization and optimization steps.
Other references provide attribution and evidence. The
[repository map](tutorial/README.md#repository-map) locates the supporting results.

## Boundaries and prior work

The channel and coherent-state description come from electron quantum optics.
The frontier quantifies restricted-source preparation at a fixed target and
full-state fidelity within that model.

A second driven input, a downstream correcting contact or a closed inner channel
changes the task. The ideal waveform class permits either sign and arbitrarily
long tails. Additional waveform restrictions retain the ideal lower bound under
the same dynamics, energy and fidelity, while attainability can change. Widening
the target changes the cost.

[Assumptions](literature/ASSUMPTIONS.md), the
[premise audit](literature/PREMISE_AUDIT.md) and
[precedent map](literature/PRECEDENT_MAP.md) distinguish formal support from
experimental ingredients. The [reading ledger](literature/PRIOR_ART.md) and
[control comparison](literature/CONTROL_PRIOR_ART.md) record inherited constructions
and the inspected sources. The [Cabart comparison](literature/CABART_2018_COMPARISON.md)
explains why closing the inner channel changes this optimization.

The [claim map](research/MODEL_AND_CLAIMS.md) distinguishes the central frontier
from general reachability and the nominal optimizer's duration/calibration
results.

## Evidence and reproduction

Use Python **3.13.5** for the recorded environment. Other environments may reproduce
the scientific assertions without identical floating-point bytes.

```sh
python -m pip install -r requirements.txt
python verify.py --integrity-only
python checks/test_repository.py
python verify.py --output-dir local-evidence-001
```

The output directory must be new. The three scientific suites cover
**6 + 7 + 5 = 18 groups**; the eight infrastructure tests are separate.
The runner retains logs and all numerical differences, checks source integrity
before and after, and never refreshes reference bytes automatically.

[Verification policy](VERIFICATION.md) distinguishes passing assertions, numerical
agreement and exact reproduction. Hosted artifacts identify their own source tree
and retain the raw comparisons for that revision.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).

The [LLM guide](llms.txt) describes relevant research questions, search terms and
the authoritative reading order for automated assistants and other readers.
The repository is available under the [MIT license](LICENSE).
