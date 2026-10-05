# Finite-energy preparation after fractionalization: a quantum-state tradeoff

**5 October 2026. Fresh Merlin–Arthur scout 09, continuing only scout 08.**

**Decision: the bounded finite-accuracy test passes. Keep this as a focused theory candidate; do not yet treat its PRL novelty or implementation as established.** The exact odd-electron obstruction does not create a fidelity ceiling below one. Instead, the declared model has a sharp, attainable source-energy versus **full outgoing-state fidelity** frontier. At fixed target width, the high-fidelity error is inversely proportional to energy. The same construction controls mean hole production. The quantum overlap, not voltage error, is the objective.

No existing research repository was accessed or modified. No new repository, manuscript, outside invitation or device proposal is created. The 12-entry scout-08 manifest, its proof and tests are preserved; the older rejected candidates remain outside this task.

## 1. Fixed model, input resources and fidelity

Retain the zero-temperature, two-channel, lossless dispersionless model of scout 08. One voltage input is controlled and the other begins in the equilibrium sea. The selected output has transfer function

\[
H_p(\omega)=p+(1-p)e^{i\omega\tau},\qquad\tau>0.
\]

The full two-input scattering matrix is unitary. For classical voltage preparation the incident bosonic density modes are coherent displacements; passive linear scattering maps them into a product of outgoing coherent displacements [G13, Eq. (20), Appendix C]. Thus the selected output is a **pure voltage-generated electronic state**, although it need not be a pure one-electron excitation. This statement is not true for arbitrary sources of injected electrons and is not extended to them here.

The input remains any real v=eV/hbar in L1(R) intersect L2(R), now with the fixed integral 2pi. Negative voltage lobes and incoming holes are allowed, as are arbitrarily long pre-emission and post-emission tails. There is no duration, peak-voltage, strict start-time, finite-temperature or drive-bandwidth constraint. Each preparation uses a fixed deterministic drive; optimizing randomized ensembles under only an average energy budget is not asserted here. The unused output is unrestricted. The energy budget is the total excess energy injected at the one driven contact,

\[
\mathcal E[v]=\frac{\hbar}{4\pi}\int v(t)^2dt.
\]

It is not electronic refrigeration heat, a Landauer cost, or an energy bound on the selected output alone. No previously checkpointed heat or memory model is imported.

Fix the target to be the charge-one Lorentzian pulse f(t)=2w/(t^2+w^2), with a fixed w>0 and time center zero. Its many-body state is a filled zero-temperature sea plus one electron in its specified normalized orbital [K06]. Denote this state by |ell_w>. Its energy is E_ell=hbar/(2w). A different width or a different electron wavefunction is a different target. Translations of the entire synthesis do not change the frontier.

The objective is the squared **many-body** overlap

\[
\mathcal F[v]=|\langle\ell_w|\Psi_{\rm out}[v]\rangle|^2.
\]

This asks for the specified electron and the rest of the sea together. It is not merely current-profile fidelity, a single-particle trace overlap with extra excitations ignored, or Hong–Ou–Mandel visibility without a state reconstruction.

## 2. Exact overlap functional, with the charge sector treated correctly

Use vhat(omega)=integral e^(i omega t) v(t)dt. Grenier et al.'s coherent displacement amplitude is -vhat/(2pi sqrt(omega)) at omega>0 [G13]. The difference between the target and actual output has zero net charge. Applying the inverse target voltage turns the state-overlap problem into the vacuum amplitude of this **neutral relative displacement**, up to an irrelevant phase. The Weyl displacement identity gives

\[
\boxed{-\ln\mathcal F[v]=D[v]
=\frac1{4\pi^2}\int_0^\infty
\frac{|H_p(\omega)\widehat v(\omega)-2\pi e^{-w\omega}|^2}{\omega}\,d\omega.}
\tag{1}
\]

The shared integer charge is essential. Individual charged pulses have an infrared singularity in a naive bosonic vacuum representation; one must not assign them a nonzero overlap with the uncharged vacuum by dropping the zero mode. A common infrared regulator cancels in the equal-charge relative expression. If the charges differ, the states occupy different charge sectors and have zero overlap. A divergent value of D likewise means F=0. The constructed pulses below have finite D.

The factor in (1) is independently fixed by two clean electron states. For widths w,W and relative displacement t0,

\[
\exp\left[-\int_0^\infty\frac{|e^{-w\omega}-e^{-W\omega+i\omega t_0}|^2}{\omega}\,d\omega\right]
=\frac{4wW}{(w+W)^2+t_0^2}
=|\langle\ell_w|\ell_{W,t_0}\rangle|^2.
\tag{2}
\]

The right side follows directly from their normalized positive-energy one-electron orbitals, with no bosonic approximation. The checker also compares a finite-circle neutral-displacement fidelity with the determinant of its fermionic occupied-space overlap. A finite bottom edge of a filled Fermi sea is avoided: the hole operator is built from cross-Fermi-level amplitudes instead. That independent check includes the actual optimized relative waveform, not only a harmonic test phase. It is a regulator check, not a finite many-electron simulation of an infinite lead.

Equation (1) is an application of inherited voltage/coherent-state theory. Neither that theory nor a new definition of quantum fidelity is being claimed as novel.

## 3. Exact optimum over arbitrary allowed inputs

Introduce dimensionless frequency x=omega tau, target ratio a=2w/tau, and

\[
A(x)=\widehat v(x/\tau)/(2\pi),\quad f_a(x)=e^{-ax/2},
\quad h_p(x)=|p+(1-p)e^{ix}|^2,
\quad U=\mathcal E\tau/\hbar=\int_0^\infty|A(x)|^2dx.
\]

The input-to-target energy ratio is R=E/E_ell=aU. For every mu>0 define

\[
\boxed{A_\mu(x)=\frac{H_p(x)^* f_a(x)}{h_p(x)+\mu x}.}
\tag{3}
\]

Here H_p(x)=p+(1-p)e^(ix); mu is a dimensionless Lagrange multiplier. The output spectral amplitude is h_p f_a/(h_p+mu x). The phase of the target is retained; narrow spectral neighborhoods of poorly transmitted frequencies are suppressed instead of being inverted at infinite cost.

For any competing A with finite D, completion of the square gives the exact identity

\[
D[A]+\mu U[A]-D[A_\mu]-\mu U[A_\mu]
=\int_0^\infty\left(\frac{h_p(x)}x+\mu\right)|A(x)-A_\mu(x)|^2dx\ge0.
\tag{4}
\]

Therefore if U[A]<=U[A_mu], then D[A]>=D[A_mu]. Equality is possible only for A=A_mu almost everywhere. This is an **all-input optimality proof**, not comparison within a selected pulse family or the result of a numerical optimization.

The optimum is physically in the previously declared waveform class. At x=0, A_mu(0)=1, giving the correct charge. Extend its spectrum by Hermitian symmetry to negative frequency to make v real. At fixed mu>0 the denominator has no real zero, the spectrum decays exponentially, and the spectrum and its first two derivatives on each frequency half-line are integrable. Integration by parts twice gives v(t)=O(t^-2), including the finite derivative jump at zero frequency. The inverse is bounded near t=0 and thus belongs to L1 intersect L2. This does not assert finite temporal support; the optimizer generally has tails on both sides of the target.

The frontier is parameterized exactly by

\[
\boxed{
R_\mu=a\int_0^\infty\frac{h_p(x)e^{-ax}}{[h_p(x)+\mu x]^2}dx,
\quad
D_\mu=\int_0^\infty\frac{\mu^2x e^{-ax}}{[h_p(x)+\mu x]^2}dx,
\quad\mathcal F_\mu=e^{-D_\mu}.
}
\tag{5}
\]

Differentiation gives U_mu'<0 and D_mu'=-mu U_mu'>0. At equal mixing, R_mu decreases continuously from infinity to zero as mu increases from zero to infinity, while D_mu increases from zero to infinity. The large-mu statements can be bounded directly by h>=const on a fixed neighborhood of zero and h<=1; they do not require abandoning the fixed charge. Thus every nonzero source budget has a unique optimal point and every fidelity strictly between zero and one is attainable at a finite energy. Perfect preparation remains impossible at finite energy.

At unequal mixing, h_p has a strictly positive minimum. The same formulas apply below the finite exact-target energy. Beyond that energy the maximum fidelity is one. For any fixed nonzero allowed error, the frontier is continuous as p approaches 1/2. The prior divergence obtained by requiring exact preparation and then taking p to 1/2 is a different order of limits.

## 4. Exact high-fidelity cost at equal mixing

Set p=1/2 and x_k=(2k+1)pi. Each transmission zero has
h(x_k+s)=s^2/4+O(s^4). Define the positive, convergent sum

\[
B(a)=\pi\sum_{k=0}^\infty\frac{e^{-ax_k}}{\sqrt{x_k}},
\qquad C(a)=aB(a)^2.
\]

The neighborhoods of these zeros give

\[
R_\mu=\frac{aB(a)}{\sqrt\mu}[1+o(1)],\qquad
D_\mu=B(a)\sqrt\mu[1+o(1)],\quad\mu\downarrow0.
\tag{6}
\]

For example, use s=2sqrt(mu x_k)y. The two universal integrals needed for energy and error are respectively integral y^2/(1+y^2)^2 dy and integral 1/(1+y^2)^2 dy, both equal to pi/2. The remaining factors evaluate at x_k. On each later period, sin^2(s/2) is bounded below by a constant times s^2 for |s|<=pi; these bounds dominate the rescaled integrals by a constant times e^(-2k pi a)/sqrt(k) away from the first interval. Their sum converges, so the local limits can be summed. The low-frequency endpoint is nonsingular and its rescaled contribution vanishes. This supplies an asymptotic argument on the complete frequency axis, not just a fit near the first notch.

Eliminating mu proves the sharp frontier

\[
\boxed{R_{\min}(\mathcal F;a)
\sim\frac{C(a)}{-\ln\mathcal F}
\sim\frac{C(a)}{1-\mathcal F},\qquad\mathcal F\uparrow1,}
\tag{7}
\]

at fixed a>0. This is both a lower bound and a constructive asymptote because of (3)–(4). A finite cutoff that skips isolated frequencies would not establish it: the cost comes from their shrinking neighborhoods.

The target duration matters strongly. At large a,
C(a)~pi a exp(-2pi a). There is no width-independent preparation-cost claim. The exact finite-fidelity values below use (5), not the asymptotic formula (7), which can be poor before the singular term dominates a finite baseline.

| Target width w/tau | F=0.99: minimum E/E_ell | F=0.999: minimum E/E_ell |
|---:|---:|---:|
| 1/8 | 21.3927 | 213.5436 |
| 1/4 | 7.6021 | 71.9086 |
| 1/2 | 1.5567 | 6.9435 |
| 1 | 0.9086 | 1.1166 |

A ratio below one at finite error is not a violation of the clean target's energy: an approximate state may have slightly lower energy than the exact target. In the exact two-input-control problem the specified target requires precisely its target energy, as already checked in scout 08.

The frequencies are integrated by geometric subdivision near each notch and ordinary adaptive quadrature inside those resolved intervals. A second integration in the original frequency coordinate agrees at representative points. Beyond cutoff X the omitted bounds are

\[
0\le R_{\rm tail}\le\frac{e^{-aX}}{4\mu X},\qquad
0\le D_{\rm tail}\le\frac{e^{-aX}}{aX}.
\]

They follow from h/(h+mu x)^2<=1/(4mu x) and the error integrand <=e^(-ax)/x. Quadrature's reported roundoff/error estimates are not exact-rational or interval certificates. The table is numerical evaluation of an analytic frontier, with refinement and tail controls explicitly distinguished.

## 5. Fidelity also controls actual holes, but is not a hole-minimization theorem

All states under discussion are pure Slater states. Let P0 be the occupied projector of the undriven Fermi sea and P*=P0+|ell><ell| that of the specified clean target. If Q is the actual occupied projector, define the physical mean hole number and target-orbital occupation by

\[
N_h=\operatorname{Tr}[P_0(1-Q)],\qquad n_\ell=\langle\ell|Q|\ell\rangle.
\]

Two same-charge Slater states can be resolved into independent rotations of occupied and unoccupied orbitals. If their squared mixing amplitudes are p_j, their squared overlap and relative missing occupation are

\[
\mathcal F=\prod_j(1-p_j),\quad
\operatorname{Tr}[P_*(1-Q)]=\sum_jp_j=N_h+1-n_\ell.
\]

This is the standard electron–hole/occupied-subspace structure [V15]; applying it relative to the target, rather than only to the equilibrium sea, avoids confusing the target electron with an unwanted particle. When D is finite the products and traces converge; otherwise the inequality below is trivial. Since -ln(1-p)>=p,

\[
\boxed{N_h+1-n_\ell\le-\ln\mathcal F.}
\tag{8}
\]

In particular the constructive optimum at F=0.999 has mean physical hole number no greater than 0.00100050034. This is a true excitation bound, not a fluence or waveform statement. It is not asserted saturated by the optimal-fidelity pulse.

There is also a simple probability statement without using the Slater decomposition. The exact target lies within the subspace with no holes, so the probability of any holes is at most 1-F. These are **unconditional** statements about the entire outgoing channel, with no temporal gate or favorable-outcome selection.

The energy in (7) is optimized for a specified many-body target fidelity, not for the smallest number of holes at any output width. Hole-free electrons with very different widths can have arbitrarily small overlap with the target. Conversely, making a broad pulse sufficiently slow can make fractionalization unimportant without delivering the specified narrow electron. Replacing one objective by the other would evade rather than solve the task.

## 6. Controls, implementation and limits

**Second contact.** Driving both inputs removes the exact obstruction by inversion of the full unitary scattering matrix; the combined source energy for outputs (target,sea) is E_ell. This is an additional independently controlled contact, not a counterexample to the one-input lower bound.

**Finite error versus exact parity.** At every fixed F<1 the one-input optimum is finite and continuous through equal mixing. Therefore the finite odd/even exact-reachability classification is not a discontinuous finite-error phase boundary. Its operational content at fixed duration is the energy-error law, not a probability ceiling.

**The rest of the device.** The other output may carry many excitations and substantial energy. Unitarity equates the total input energy to both output energies together. Fidelity is demanded only in the selected output; no claim is made that the full two-channel state equals one electron plus two untouched seas.

**Duration and dispersion.** The optimized waveform has tails, with increasingly narrow compensating frequency features at high fidelity. Their implementation can require a long coherent control interval. No finite-start, finite-duration, peak-amplitude, finite-temperature, nonlinear-band, dispersive-mode or calibrated-contact error model has been solved. Such added restrictions can only worsen the ideal optimum, but the optimum itself need not be attainable with them. A table in dimensionless units is not a device-performance forecast.

**No independent phase-noise assumption.** Voltage shaping uses a prescribed coherent drive. Random classical pulse jitter, thermal density modes or uncontrolled environment excitations would change the state and hence its fidelity formula. They have not been asserted harmless. No experiment is logically required for the conditional theorem, but the requested model-matched premise precedents and a joint operating window remain incomplete.

## 7. Novelty assessment and the bounded decision

The source hierarchy is explicit. Keeling–Klich–Levitov supplies the clean target class; Grenier et al. supplies the exact channel model, voltage-to-coherent-state correspondence and ordinary fractionalization; Vanevic et al. supplies the electron–hole decomposition; Roussel et al. studies extraction and characterization of the single-particle content of currents. None of these ingredients is claimed new.

The optimization in (4) is elementary completion of a quadratic form. This is not a new inverse-problem algorithm or a new coherent-state fidelity formula. The candidate increment is the complete finite-energy frontier for the prescribed physical synthesis problem, the exact high-fidelity coefficient, and the implication for actual electron/hole cleanliness. It is not enough merely to rename a voltage least-squares cost: the 1/omega weight, equal-charge condition and hole relation are essential to this being a quantum-state result.

The inspected passages of G13 give fractionalization and its special input-pulse lines, not the arbitrary-input energy-constrained target optimum here. Roussel et al. [R21] and Cabart et al. [C18] remain only abstract/selected-scope comparators in this pass because their full author files were not available through the requested routes. The latter changes geometries or interaction/environment properties to control decoherence; it is not treated as a proved exclusion of this fixed-control problem. The complete source-control citation chain is **not** audited. No absence claim is based on failed searches, failed PDF screenshots or irrelevant electrical-product results for the word leviton.

**Decision: scientific GO from the exact-reachability scout to a finite-accuracy theory candidate.** The stipulated finite-accuracy test has an affirmative result with a meaningful cost for short fixed target pulses. It is not only an isolated exact zero with no finite-error consequence. On the other hand, broad target pulses make the cost small, a second control removes the obstruction, and the proof tools are standard. PRL significance and precise priority remain unsettled. No dedicated repository or manuscript is selected by this pass.

The next bounded decision is to compare this explicit **quantum-state energy frontier**, not the old parity slogan, against the closest pulse-control literature and to decide whether its physical consequence warrants a dedicated project. Do not add an extra channel, a new interaction model or numerical pulse-shaping campaign to make the question survive. If it is already an immediate stated control result or a benefit outside any credible fixed-target regime, checkpoint it. A genuinely separate proof reader is still absent; no invitation is authorized.

## 8. Reproduction and access record

The seven new groups test the coherent/fermionic normalization; Slater hole and overlap identities; exact global-optimum completion; independent quadrature and total-energy accounting; high-fidelity coefficient; the finite-fidelity table and continuity; and control/metric boundary cases. They include a 256-mode fermionic determinant regulator and one-dimensional integrals, not a large many-electron simulation. The prior six scout-08 groups are rerun unchanged. All universal claims above follow from the proof, not these finite examples.

The first new script's assertions passed, but its tangent-mapped quadrature emitted warnings in some narrow-notch evaluations. The final implementation uses geometric subdivision in the original frequency coordinate, retaining the same formulas and tolerances. Warnings disappeared and representative values agree with independent quadrature. The warning-bearing script/log/report and the explicit refinement patch are retained, rather than silently treating the first run as warning-free. The subsequent independent fermionic-waveform crosscheck was added within the existing group; no claimed number of new groups was inflated.

SOURCES.json states actual primary reading depth. Requested PDF screenshots failed; parsed text is not described as visually verified. Publication PDFs and fonts are not included in the deliverables. The original source archive, checkpoints and unrelated repositories remain unchanged.

### Primary attribution

[G13] C. Grenier et al., *Fractionalization of minimal excitations in integer quantum Hall edge channels*, PRB 88, 085302 (2013), [author PDF](https://arxiv.org/pdf/1301.6777). Re-read III.B Eqs. (19)–(22) and Appendix C coherent scattering, with the earlier finite-source and electron/hole context. The mode amplitude in Eq. (20) fixes (1)'s normalization. No figure-derived number is imported.

[K06] J. Keeling, I. Klich and L. S. Levitov, *Minimal excitation states of electrons in one-dimensional wires*, PRL 97, 116403 (2006), [author PDF](https://arxiv.org/pdf/cond-mat/0604017). Minimal phase and single-electron construction, previously read and rechecked for the target convention. This target is not new.

[V15] M. Vanevic, J. Gabelli, W. Belzig and B. Reulet, *Electron and electron-hole quasiparticle states in a driven quantum contact*, [author PDF](https://arxiv.org/pdf/1506.03878). Re-read the many-body form and the paired occupied/unoccupied decomposition, Eqs. (1)–(3). Periodic examples and measured tunnel-junction parameters are not transplanted into a finite-pulse implementation. The note's target-relative trace inequality is derived above.

[I97] D. A. Ivanov, H. W. Lee and L. S. Levitov, *Coherent states of alternating current*, PRB 56, 6839 (1997), [primary publisher record](https://doi.org/10.1103/PhysRevB.56.6839). Abstract and publication metadata only; inherited pulse optimization/statistics context, not a full theorem comparison.

[R21] B. Roussel et al., *Processing Quantum Signals Carried by Electrical Currents*, PRX Quantum 2, 020314 (2021), [primary article record](https://journals.aps.org/prxquantum/abstract/10.1103/PRXQuantum.2.020314). Abstract, popular summary and displayed reference list. Author arXiv:2008.01580 abstract was read; full HTML/PDF requests failed. This is not a full source-level exclusion of an overlap.

[C18] C. Cabart et al., *Taming electronic decoherence in one-dimensional chiral ballistic quantum conductors*, PRB 98, 155302 (2018), [primary publisher abstract](https://journals.aps.org/prb/abstract/10.1103/PhysRevB.98.155302), author arXiv:1804.04054. Abstract and metadata only; direct author PDF retrieval failed. Circuit/environment strategies differ in their stated scope; no comprehensive priority certificate is asserted.
