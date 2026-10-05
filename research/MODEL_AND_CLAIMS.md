# Model, claims and proof dependencies

**5 October 2026. Frontier, planning and bounded physical-premise audits completed.**

## Question and allowed resources

How much total excess energy must one upstream voltage source inject to prepare one prescribed downstream electron wavepacket after a fixed two-channel interaction? Both channels remain open. The state reference is the zero-temperature Fermi sea. The second input receives no voltage. The unused output is not constrained to remain a sea.

The input is real $v=eV/\hbar\in L^1(\mathbb R)\cap L^2(\mathbb R)$ with integral $2\pi$, with polarity chosen so that positive charge-one pulses inject electrons. Either sign, incoming holes, and arbitrarily long predetermined tails are permitted. It is a deterministic waveform, not a randomized strategy constrained only on average. The target is the voltage-generated charge-one Lorentzian with fixed width $w>0$ and fixed center after removing a common delay. Its energy is $\mathcal E_\ell=\hbar/(2w)$.

The effective output voltage is $pv(t)+(1-p)v(t-\tau)$, $0\le p\le1$, $\tau>0$. The weight $p$ describes collective modes; it is not an individual electron's path probability. The two-port scattering matrix is unitary. The energy $\mathcal E_{\rm in}=\hbar\int v(t)^2dt/(4\pi)$ counts excess energy launched into the driven incoming edge, including energy eventually carried by the unused channel. It is not the full electrical work of the bias circuit, heat production or a cost charged only to the selected output; see the [premise accounting check](../literature/PREMISE_AUDIT.md#4-energy-convention-and-accounting-check).

## Operational objective

The selected voltage-generated output remains pure in the stipulated linear coherent-state model. For finite relative displacement norm, the objective is $\mathcal F=|\langle\ell_w|\Psi_{\rm out}\rangle|^2$: the target electron *and* its sea. On the full waveform class it is the common-infrared-regulator limit $\mathcal F=e^{-D}$; for $D=\infty$ this is zero, without asserting a ket in the target representation. Correct charge and finite source energy alone do not ensure finite $D$. A current profile, first-order coherence overlap, HOM visibility and this many-body overlap are not interchangeable. General non-voltage single-electron sources need not remain pure after tracing the other channel.

With the Fourier sign $e^{+i\omega t}$, set $x=\omega\tau$, $a=2w/\tau$, $A=\widehat v/(2\pi)$ and $f_a=e^{-ax/2}$. Equal charges must be retained when deriving

```math
D[A]=\int_0^\infty\frac{|H_pA-f_a|^2}{x}dx,\qquad
R[A]=a\int_0^\infty|A|^2dx,\qquad H_p=p+(1-p)e^{ix}.
```

A neutral *relative* displacement justifies this expression. A charged state's overlap with an uncharged bosonic vacuum is not substituted for it. Divergent $D$ means zero fidelity.

## Claim hierarchy

| ID | Statement and status | Author-side proof | Supporting suite |
|---|---|---|---|
| C1 (central) | Exact all-waveform energy–fidelity frontier and an admissible constructive optimum at positive energy. | [Frontier](FIDELITY_FRONTIER.md), Sections 2–4. | `checks/check_finite_accuracy.py`, 7 groups. |
| C2 | At equal splitting and fixed target width, $R_{\min}\sim C(a)/[-\ln\mathcal F]$; no finite-energy exact one-electron inverse. | [Frontier](FIDELITY_FRONTIER.md), Section 4; [Reachability](EXACT_REACHABILITY.md), Section 3. | Finite-fidelity and reachability. |
| C3 | Actual hole contamination obeys $N_h+1-n_\ell\le-\ln\mathcal F$; any-hole probability is at most $1-\mathcal F$. | [Frontier](FIDELITY_FRONTIER.md), Section 5. | Fermionic/Slater controls within finite-fidelity. |
| C4 (support) | Finite clean-target reachability at equality is an alternating multiplicity condition; asymmetry restores the exact inverse. | [Reachability](EXACT_REACHABILITY.md), Sections 4–5. | `checks/check_pulse_reachability.py`, 6 groups. |
| C5 (qualification) | Exact splitting-miscalibration penalty and energy-weighted duration of the nominal energy optimizer. | [Optimizer limitations](OPTIMIZER_LIMITATIONS.md), Sections 3–5. | `checks/check_control_audit.py`, 5 groups. |

C1 needs the inherited pure coherent-state transfer, equal-charge overlap normalization, and the optimization identity. Its existence argument also needs the inverse waveform to belong to the stated $L^1\cap L^2$ class. C2 adds isolated-zero asymptotics over the complete frequency axis. C3 separately needs the Slater-state/occupied-space argument. C5 is not a replacement novelty claim. The [bounded author-side audit](FRONTIER_AUDIT.md) has now checked C1–C2's three dependencies and supplied explicit bounds. It found the infrared qualification above, with no change to the frontier or its coefficient; see the [change record](../provenance/FRONTIER_AUDIT_CHANGE.md). C3's separate occupied-space proof was not certified by this task. Passing tests is not an independent proof of these implications.

## Controls and orders of limits

At exact equality, finite clean odd-electron targets are excluded. At every fixed nonzero allowed error the cost is finite and continuous in $p$. These are different limits, not a finite-error parity phase transition. Widening the target changes the optimization task.

Two independent upstream inputs can invert the full unitary matrix. A downstream voltage can cancel distortion after it occurs. Closing the inner channel changes the transfer function. All three are outside the fixed control/geometry specification, not contradictions of the bound. A long delayed compensating excitation cannot be ignored by a time gate when claiming global state fidelity.

No optimal minimum duration, minimax-robust solution, causal-start theorem, thermal-state result, arbitrary-source result, detector theorem or achieved performance is included. Adding waveform restrictions under the same dynamics, energy and objective keeps the ideal optimum as a lower bound but may remove attainability. Changed dynamics or a thermal target do not automatically inherit that bound.

## Originality and current limit

The ensemble preparation, clean Lorentzian criterion, bosonization, channel and correction frameworks are inherited. The optimization is elementary completion of a quadratic form. The candidate contribution is the particular complete restricted-source preparation law and its quantum-state/hole interpretation. [PRIOR_ART](../literature/PRIOR_ART.md) states the actual comparison depths. No first-ever or exhaustive novelty certificate is claimed.

The [manuscript plan](MANUSCRIPT_PLAN.md) implements the bounded GO from [SIGNIFICANCE](SIGNIFICANCE.md). It uses C1–C2 as an exact ideal feasibility statement at fixed target, transfer and fidelity, with the optimizer's output-energy allocation and two-input comparison explaining the restricted-access cost. Neither consequence is a new general optimization principle. C3 is omitted from the planned argument, with its separate proof check still open. The [premise audit](../literature/PREMISE_AUDIT.md) retains this conditional wording and separates inherited formal support from experimental ingredients. Independent critical reading, priority, substantial impact, a joint operating regime and the broader precedent benchmark remain open; no manuscript, release or expanded model is initiated.
