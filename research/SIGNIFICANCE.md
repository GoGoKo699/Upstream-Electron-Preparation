# Significance assessment of the fixed preparation law

**5 October 2026. Decision: GO to bounded manuscript planning around C1–C2.**

Assessed base: `ca492b05f0ddc3cabd99d8a82dd21fe8381ed011`, tree
`ac8930712b2e762e156617501c2c7700659b2eae`. This is an author-side judgment
about the value of the fixed result. It is not a priority certificate,
independent scientific review, or a decision to submit a manuscript.

## The central physical statement

In the fixed lossless two-open-channel model, access to only one upstream
voltage source imposes a sharp energy cost for preparing a prescribed clean
outgoing Lorentzian electron, including its Fermi sea. At equal splitting,
perfect preparation has no finite-energy solution. Every fidelity below one
is nevertheless attainable, and at fixed target width the optimal source cost is

```math
\frac{\mathcal E_{\min}}{\mathcal E_\ell}
\sim\frac{C(2w/\tau)}{-\log\mathcal F}
\sim\frac{C(2w/\tau)}{1-\mathcal F}.
```

The value is the complete preparation statement: the cost is a lower bound
over the entire declared waveform class, and an admissible pulse attains the
finite-error frontier. A singular exact inverse alone would not quantify the
best approximate preparation. The [frontier](FIDELITY_FRONTIER.md) and
[audit](FRONTIER_AUDIT.md) supply both directions.

The source may already generate holes, use negative voltage and have
arbitrarily long predetermined tails. The conclusion therefore does not depend
on choosing a poor finite pulse family. Fixing the target orbital and sea also
prevents changing the task by broadening the electron or ignoring a delayed
compensating excitation.

## What is elementary, and what remains useful

Once the inherited coherent-state metric and transfer function are given,
the optimizer follows by quadratic completion. The inverse-error exponent
comes from simple zeros of the transfer amplitude. Neither is a new general
optimization method or a uniquely fermionic scaling mechanism.

The quantum content enters through the precise preparation objective and its
connection to an experimentally motivated electron source model: the error is
the overlap with one specified electron and an otherwise correct sea. The
candidate contribution is the sharp restricted-source law for that task,
including attainability, source-energy accounting and its singular endpoint.
This is enough for a focused theory manuscript to be assessed on its merits.
It does not establish broad impact simply because the state is many-body.

There is a useful physical contrast already in the fixed model. Driving both
inputs prepares the exact target at combined energy $\mathcal E_\ell$; with
one input at equal splitting, the energy diverges as fidelity tends to one.
The [two-control construction](EXACT_REACHABILITY.md) makes the changed resource
explicit. The selected voltage-generated state remains pure, and the full
scattering is unitary. The limitation concerns accessible control.

The [energy allocation calculation](FIDELITY_FRONTIER.md#6-controls-implementation-and-limits)
makes this interpretation concrete: along the optimum, the selected-output
energy is bounded by $\mathcal E_\ell$ and tends to it, while the unused-output
energy diverges with the source cost. That is a direct corollary of the existing
optimizer and unitarity, not a separate novelty claim or a heat-production law.

## Closest comparisons and what they rule out

Source-derived statements in the middle column are distinguished from our
comparison in the right column. Keys resolve in the [prior-art ledger](../literature/PRIOR_ART.md).

| Source and primary passage | What was already done | Consequence for this candidate |
|---|---|---|
| [L11](https://arxiv.org/pdf/1103.4046), Eqs. (4), (6), (7); p. 3 after Eq. (11). | Maximizes a full many-body restoration overlap using a downstream voltage and reaches unit modulus. Its single-channel response in Eq. (7) has unit modulus. MZI visibility instead uses half the restoration phase. | We cannot claim first fidelity-based voltage correction. Moving a control upstream alone is not the distinction: its all-pass response has no transmission null. The selected port of our open two-channel device and the imposed source-energy budget matter together. Its partial MZI restoration is not our fidelity ceiling. |
| [R21](https://journals.aps.org/prxquantum/pdf/10.1103/PRXQuantum.2.020314), Secs. IV.B and V.A.1–2, Eqs. (43)–(45), Fig. 5; Appendix G opening. | Optimizes mesoscopic-capacitor amplitude and QPC transparency through electron–hole entropy for sine driving, with a square-drive comparison. This inspected optimization fixes frequency/geometry, without a prescribed target overlap or injected-energy budget. | Source optimization and many-body source-quality objectives are already established. Those parameter/objective choices do not supply the arbitrary-waveform, fixed-energy preparation frontier studied here. |
| G13 and C18, as already recorded in the [construction comparison](../literature/CABART_2018_COMPARISON.md). | Supply the open-channel transfer and voltage-driven coherent-state picture; C18 also studies a closed inner channel. | The propagation model and purity are inherited. Closing the channel changes the transfer and allowed device; that construction does not establish our fixed open-channel cost. |

**Reading depth in this pass:** L11's four-page primary paper was read, with
equation and geometry checks. R21's relevant entropy/source-analysis sections
and Appendix G opening were checked; this is not a full appendix or numerical
reproduction. C18 was not reopened: its supplied-paper construction audit remains
the authority at its recorded depth. No new negative claim is made about all
contents of these papers or about every earlier source.

Targeted discovery searches for upstream compensation, fractionalization and
energy/fidelity optimization returned substantial irrelevant material. They
provide no negative novelty evidence. The decisive comparison here uses the
identified primary passages. One L11 HTML request failed and the R21 DOI landing
request returned 403; their direct primary PDFs were subsequently accessible.
There is no unresolved access gap for the passages used above.

## Strongest reason to hold, and the decision

The strongest objection is that an informed reader can regard the work as a
direct application of standard regularized inversion to known electron optics.
The exact divergence also uses equal splitting. At fixed nonzero error the
frontier is continuous in splitting, and known asymmetry restores a finite-energy
exact inverse. Broad targets suppress the coefficient exponentially. Long tails
and calibration requirements limit an apparatus interpretation. Additional
decimal places, the parity classification, or nominal duration formulas would
not answer this objection.

The reason to proceed is narrower: C1–C2 completely answer an identifiable
state-preparation question within a familiar ideal model, with a lower bound,
attaining waveform and explicit accounting of where its energy goes. A reader
can use the result as an optimistic benchmark for one-contact preparation;
additional restrictions on the same waveform problem cannot lower its minimum.
Changing the dynamics or fidelity definition is a different problem, for which
the bound need not apply. The physical conclusion can be stated and evaluated
without promoting the solution method to a new principle.

**GO means prepare a claim-driven manuscript plan for this contribution.** It
does not mean that novelty, practical performance or publication suitability
has been established. The independent critical reading and model-matched
physical-premise evidence remain open. A directly covering earlier result would
require revisiting the originality assessment. No experiment is required for
the conditional theorem, and no achieved preparation or direct fidelity detector
is claimed.

## Claim priorities and stopping point

| Material | Role in planning |
|---|---|
| C1–C2 | Central claim: exact source-energy/full-state-fidelity frontier, attainable control and fixed-width endpoint. |
| One-input/two-input comparison and optimal-output energy accounting | Explain why the cost measures restricted access in a unitary device. These are supporting consequences. |
| C3 | Optional hole interpretation; its separate occupied-space proof is not certified by the frontier audit and is not needed for this significance decision. |
| C4–C5 | Supporting reachability and limitations. They do not replace the central claim or rescue its significance. |

This pass adds no model, objective, optimization campaign, scientific test group
or changed reference value. The only added displayed consequence in the proof
route is the optimizer's output-energy allocation, derived directly from the
existing formulas. The source-energy frontier and infrared qualification are
unchanged. The requested significance decision is complete; stop here and use
the single [next work order](../work_orders/CURRENT.md) for manuscript planning.
