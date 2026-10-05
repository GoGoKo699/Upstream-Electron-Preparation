# Upstream electron-state preparation: control location, calibration, and duration

**5 October 2026 — fresh Merlin–Arthur scout 10.**

**Decision: GO for focused theoretical development of the fixed one-input preparation problem.** The exact finite-energy fidelity frontier survives the targeted predecessor comparison. The new checks expose the calibration and duration needed by its optimizer; they do not certify an apparatus or a more general robust-control optimum. PRL suitability and global priority remain provisional. No repository, manuscript, outside contact, or previous-project modification is part of this pass.

## 1. The question is where control is available, not whether evolution is reversible

The system is the same zero-temperature, lossless, dispersionless two-channel fractionalization model as scouts 08–09. A real deterministic voltage can be applied only to one upstream input. The other input remains at equilibrium. The target is one prescribed clean Lorentzian electron above the Fermi sea in a selected downstream channel, with no added holes in that entire channel. No restriction is placed on the unused output. Voltage lobes of either sign and arbitrarily long preparation tails are allowed. No downstream correction contact or second driven input is available.

The channel, the coherent-state voltage representation, and clean Lorentzian electron sources are inherited [G13,K06,D13]. The scoped proposed result is the energy required to reach a specified full many-body target under that control restriction. It is neither a new fractionalization mechanism nor evidence of irreversible many-body decoherence in the voltage-generated class.

A source-level predecessor matters here. Grenier et al. [G13], Section III.A.2, derive the effective output voltage and point to correction by an appropriate pulse. Their cited reference 67 is Lebedev–Blatter [L11]. Reading that paper's Eqs. (2)–(7) and its correction geometry resolves an apparent conflict: it maximizes the many-body overlap after applying a correcting voltage **downstream** of the interacting region, in its one-edge capacitive model. It obtains unit overlap. That is an important known control possibility, not a theorem that an arbitrary desired signal can be produced by a finite-energy upstream-only inverse of a two-mode transfer function with real-frequency zeros.

For our model this distinction is elementary. If the incident voltage is f and the outgoing voltage is Hf, a downstream actuator can add (1-H)f. The selected output becomes f exactly. At equal splitting this correction is one half of a Lorentzian minus its delayed copy: a finite-energy neutral pulse. Allowing that actuator changes the available control ports, so it is outside the one-input bound. The norm of an applied correction waveform is not automatically the net work it performs on an already excited channel; no new energy accounting for that modified setup is claimed.

Thus the theory does not contradict the possibility of undoing voltage-generated distortions. Its contribution must be stated as an **upstream-control resource law**.

## 2. Fixed mathematical statement from scout 09

Write x=omega*tau, a=2w/tau>0, and f_a(x)=exp(-a*x/2). The Fourier transform uses exp(+i omega t). In units where A(x)=vhat(x/tau)/(2*pi), v=eV/hbar, the selected transfer is

\[
H_p(x)=p+(1-p)e^{ix},\qquad h_p=|H_p|^2.
\]

The prescribed target has total charge one electron and energy E_l=hbar/(2w). Relative coherent displacements are neutral. The many-body fidelity and source energy are

\[
D[A]\equiv-\ln F[A]=\int_0^\infty\frac{|H_pA-f_a|^2}{x}\,dx,
\qquad R[A]\equiv\frac{E_{\rm in}}{E_l}=a\int_0^\infty|A|^2dx.
\]

The 1/x weight is quantum-state overlap, not ordinary waveform error. The optimizer for every positive multiplier mu is

\[
A_\mu(x)=\frac{H_p(x)^*f_a(x)}{h_p(x)+\mu x}.
\]

Completing the square proves global optimality over the declared input class. At p=1/2, the transmission zeros x_k=(2k+1)pi give

\[
B_0(a)=\pi\sum_{k\ge0}\frac{e^{-a x_k}}{\sqrt{x_k}},\quad
D_\mu\sim B_0\sqrt\mu,\quad
R_\mu\sim\frac{aB_0}{\sqrt\mu},\quad
R_{\min}(F;a)\sim\frac{aB_0(a)^2}{-\ln F}.
\]

The pure-state and Slater structure also gives the previously established hole bound N_h+1-n_l <= -ln F. Neither the frontier nor that bound optimizes hole number independently of the target wavefunction. The exact target is unattainable with finite energy at equal splitting, but every fixed F<1 is attainable in the model. Changing the target width changes the cost.

All these statements, their finite input-class qualifications, and the original checks remain in the untouched scout-09 archive. This round does not quietly replace them by a finite-duration pulse or a mixed-temperature state.

## 3. Exact sensitivity of the nominal energy optimizer

The nominal device has p=1/2. Let the actual device have p=1/2+epsilon with the same delay tau, while the voltage remains the pulse designed for nominal equality. This is a deterministic calibration error in an existing parameter, not a new stochastic bath model. No change is made to the target or total input charge.

Set H_0=e^{ix/2}cos(x/2), h=cos^2(x/2), and G=1-e^{ix}. The nominal residual and the parameter derivative obey

\[
H_0A_\mu-f_a=-\frac{\mu x f_a}{h+\mu x}\in\mathbb R,
\qquad
GA_\mu=-\frac{2i\sin(x/2)\cos(x/2)f_a}{h+\mu x}\in i\mathbb R.
\]

Their cross term vanishes at every frequency. Therefore, for the entire allowed range |epsilon|<=1/2,

\[
\boxed{D_{\rm actual}(A_\mu)=D_\mu+\epsilon^2K_\mu,\qquad
K_\mu=4\int_0^\infty
\frac{h(1-h)e^{-a x}}{x(h+\mu x)^2}\,dx.}
\tag{1}
\]

This is exact in the same model, not a first-order expansion in epsilon. The integral is finite for every mu>0; near zero its integrand is O(x). It quantifies the fidelity of the **fixed nominal optimizer**, not the optimum for the actual asymmetric channel and not a minimax-robust design.

Define

\[
B_1(a)=\pi\sum_{k\ge0}\frac{e^{-a x_k}}{x_k^{3/2}}.
\]

Near a node x_k+s, h=s^2/4+O(s^4). With c_k=2*sqrt(mu*x_k), the leading term of the K integrand is 16*exp(-a*x_k)*s^2/[x_k*(s^2+c_k^2)^2]. Since the integral of s^2/(s^2+c_k^2)^2 over the line is pi/(2c_k),

\[
K_\mu\sim\frac{4B_1}{\sqrt\mu},\qquad
\boxed{D_\mu K_\mu\longrightarrow4B_0B_1.}
\tag{2}
\]

The exponentially decreasing node weights make the residue sum convergent. One can first control finitely many isolated nodes, bound the remaining local contributions by their summable exponential weights, and separate the very large x region, where the exponential beats the inverse powers of mu. The nonsingular near-zero and inter-node contributions are subleading. This is the same fixed-width limit as in scout 09, not a simultaneous large-width assertion.

At fixed a, keeping the calibration penalty negligible relative to the nominal D requires epsilon=o(D) for this optimizer family. A simple finite prescription is

\[
|\epsilon|\le\sqrt{\frac{q D_\mu}{K_\mu}}
\quad\Longrightarrow\quad D_{\rm actual}\le(1+q)D_\mu.
\tag{3}
\]

For q=0.1 and a nominal fidelity 0.999, the guaranteed fidelity is 0.999^1.1, approximately 0.9989001. This budget is 10% additional **log infidelity**, not a claim of keeping the final fidelity exactly at the nominal value.

A known nonzero p-1/2 allows a redesigned inverse and removes the exact transmission zeros. Consequently (1)–(3) are not a fundamental assertion that every departure from equal splitting worsens preparation. They are a warning against applying an extremely sharp nominal compensation to an inaccurately calibrated device. For fixed nonzero epsilon, decreasing mu sufficiently far eventually drives D_actual upward, even while the nominal D approaches zero.

## 4. The pulse's energy-weighted duration is also singular

Long preparation tails were already allowed, but the numerical energy table did not quantify how much of the pulse they carry. Define a normalized source-energy profile proportional to v(t)^2 and its variance

\[
\bar t=\frac{\int t v(t)^2dt}{\int v(t)^2dt},\qquad
\sigma_t^2=\frac{\int(t-\bar t)^2v(t)^2dt}{\int v(t)^2dt}.
\]

This is not the charge density of the electron, a detector gate length, or a hard support interval. The existing optimal voltages have sufficiently decaying tails for these moments. In dimensionless form write

\[
A_\mu(x)=e^{-ix/2}b_\mu(x),\quad
b_\mu(x)=\frac{\cos(x/2)e^{-a x/2}}{\cos^2(x/2)+\mu x},\quad x>0,
\]

with b extended as a real even function. Parseval's identity gives, relative to the centered target and after removing the common propagation delay,

\[
\boxed{\bar t=-\tau/2,\qquad
\frac{\sigma_t^2}{\tau^2}=\frac{\int_0^\infty|b_\mu'(x)|^2dx}{\int_0^\infty|b_\mu(x)|^2dx}.}
\tag{4}
\]

The negative mean time reflects predetermined precompensation, not signaling backward in time. A positive-frequency derivative jump at zero is treated through the continuous, even extension; it does not create a delta function in the first weak derivative.

Near a transmission zero, b is, up to its sign, 2*exp(-a*x_k/2)*s/(s^2+c_k^2). Its derivative is 2*exp(-a*x_k/2)*(c_k^2-s^2)/(s^2+c_k^2)^2. The elementary integral

\[
\int_{-\infty}^\infty\frac{(1-y^2)^2}{(1+y^2)^4}dy=\frac\pi4
\]

yields

\[
\int_0^\infty|b_\mu'|^2dx\sim\frac{B_1}{8\mu^{3/2}},\quad
\boxed{\frac{\sigma_t}{\tau}\sim\frac1{\sqrt\mu}\sqrt{\frac{B_1}{8B_0}},
\qquad D_\mu\frac{\sigma_t}{\tau}\to\sqrt{\frac{B_0B_1}{8}}.}
\tag{5}
\]

The same isolated-zero/tail argument applies. For an explicit high-frequency tail X, direct differentiation bounds |b'| by exp(-ax/2)*[(1+a)/(2mu*x)+(1/2+mu)/(mu^2*x^2)]. Squaring with (u+v)^2<=2u^2+2v^2 bounds the omitted derivative-norm integral. The independent K tail is at most exp(-aX)/(a*mu*X^2). These analytic omitted-tail bounds accompany the quadrature; floating-point roundoff is not interval-certified.

Equation (5) describes the unique nominal energy optimizer. It is not a proof that every pulse with a given fidelity must have this minimum duration. A different energy, causal-start, bounded-duration, or robust-control problem would have to be posed separately. None is silently solved here.

## 5. Finite target values and their interpretation

For nominal fidelity 99.9%, refined one-dimensional integrals give:

| Target w/tau | Energy E_in/E_l | Source sigma_t/tau | Absolute p error allowing 10% extra log infidelity |
|---:|---:|---:|---:|
| 1/8 | 213.5436 | 176.0128 | 0.00031774 |
| 1/4 | 71.9086 | 74.4513 | 0.00074761 |
| 1/2 | 6.9435 | 14.0812 | 0.00347647 |
| 1 | 1.1166 | 0.9369 | 0.01855291 |

These p errors are absolute fractions, not relative percentage errors on p. In the first row an actual p=0.501, used with the pulse designed for p=0.500, gives F_actual=0.9980105075. The pulse energy has not changed. Reoptimizing for the known actual p is a different calculation and may improve fidelity.

The broad-target rows are not all in the same high-fidelity asymptotic regime as the short-target row at this particular F; the exact integrals, not Eq. (5) alone, produce the table. The width sensitivity was already present in scout 09. No laboratory time in seconds or attainable voltage precision has been assumed. The source RMS width does not specify a sharp truncation length.

The bound E_in/E_l>=213.54 for the first row remains a true optimistic benchmark when extra source constraints are imposed: restricting the allowed waveforms cannot lower its ideal minimum. However, the displayed ideal waveform is not automatically admissible with finite bandwidth, finite start time, finite voltage range or limited coherence. Those restrictions can change achievable fidelity and the optimizer.

## 6. Construction-level novelty assessment

The accessible predecessors resolve several potential overlaps, but not all of them.

**Ivanov–Lee–Levitov [I97].** Appendix C explicitly minimizes transferred-charge variance at fixed average transferred charge, using analyticity of phase factors. This is an important pre-existing optimal-pulse problem, not just a general noise discussion. It does not impose our source-energy budget or target a specified outgoing many-body electron orbital through a fixed interacting filter. The clean Lorentzian and analytic phase criteria remain inherited.

**Lebedev–Blatter [L11].** Their Eqs. (2)–(7) already optimize many-body overlap and restore a scattered Lorentzian wavepacket with a downstream correcting voltage. Thus we cannot claim the first use of exact overlap to correct an electronic source. The location of the control, the single-edge all-pass interaction model, and the absence of our input-energy constraint are the substantive distinctions. Our obstruction is not a contradiction of their restoration theorem.

**Grenier et al. [G13].** Their source-to-output coherent-state relation and the exact two-mode scattering matrix are the ingredients of our model. Their paper treats special clean fractionalization/revival patterns, finite temperature and other interaction ranges. Its correction statement cites L11. We inherit this framework rather than discover reversibility or clean even-charge outputs. The all-input finite-energy frontier is the result being assessed, not any of those ingredients.

**Roussel et al. [R21].** The full 36-page publisher article is now accessible. It decomposes periodic electronic coherence into elementary excitation modes and uses electron–hole entanglement entropy to assess sources. Section V.A.2 actually optimizes mesoscopic-capacitor transparency and drive amplitude using an entropy objective. Therefore it would be inaccurate to say it contains no optimization. The inspected construction does not give our arbitrary-waveform, fixed-energy, upstream-only many-body fidelity frontier. No numerical figure/table comparison or full appendix reproduction is claimed.

**Cabart et al. [C18].** The primary abstract describes material/sample design and a closed-edge geometry to reduce decoherence. Full-text arXiv and publisher retrieval repeatedly failed; only the abstract and bibliographic record were read. Its full construction remains a priority-check gap. The fact that its abstract emphasizes a different control strategy does not exclude every theorem in its full text.

The targeted searches did not find the exact source-energy frontier in the accessible constructions. This is not a global priority certificate. A theorem in an uninspected source or an older control treatment could still subsume it. The newly exposed calibration and duration formulas use elementary linear-system and Fourier methods; they are practical qualifications of the central result, not a replacement novelty claim.

## 7. Decision and the appropriate next commitment

**GO for a dedicated, fixed-scope theoretical candidate.** The reason is the complete operational statement: one specified clean electron, actual many-body fidelity and hole contamination, a quantified resource budget, a bound covering every allowed upstream waveform, and a constructive optimum. The exact-reachability restriction alone would have been less persuasive; the finite-accuracy result makes it an operational cost question. The simple mathematics is an advantage if the physical statement is new and important, not evidence by itself against a theory Letter.

The strongest editorial objection is that the problem could be viewed as standard regularized inversion of a known transfer function, with quantum physics entering mainly through the weighted fidelity functional. The modest claim must meet that objection through its specific preparation limitation, not by adding mathematical ornament. A source-energy/fidelity result should not be advertised as a fundamental energy cost of an electron, irreversible decoherence, or an implementation already shown feasible.

The 2011 comparison removes a misleading broad headline: interaction-induced distortions can be correctable with an additional downstream control. Our result concerns which restricted source can supply that correction before propagation, and at what energy, duration and calibration cost. Those are explicit boundaries of the result, not unexplained exceptions.

The mathematical core is now coherent enough for a claim-driven research record and critical review. It does not need another pulse-shape sweep, another channel, or a new platform to prolong the scout. A new repository is organizationally appropriate only after the owner selects and authorizes its destination. No repository has been created or touched here. A separate reviewer has not been contacted. Manuscript drafting is not initiated.

Before a submission decision, the outstanding C18 construction-level access, a genuine independent check of the overlap/optimization assumptions, and a precise significance assessment remain necessary. The model-specific preparation and operating assumptions have not passed a complete five-to-ten-primary-precedents-per-convention audit. A theory result needs no experiment to be correct, but no achieved 99.9%-fidelity device is inferred from our table.

## 8. Reproduction and primary attribution

`python check_control_audit.py --output NEW.json` runs five groups: exact calibration identity and time convention; direct actual-channel overlap; independent derivative/time-moment integration; derived asymptotic constants; and the finite-target/calibration controls. All passed on the first run and repeat. `control_integrals.py` implements resolved, pole-aware scalar integrals with analytic discarded-frequency bounds. Quadrature error estimates are diagnostics, not interval-certified numerical errors.

The previous seven finite-accuracy groups and six exact-reachability groups were rerun unchanged; their reports match their stored reports byte-for-byte. All 39 entries in the prior scout-09 manifest remain unchanged. No old scientific repository or other candidate's code is used. Sources, failed access and exact comparison depth are recorded in SOURCES.json. No publication PDF is redistributed.

[I97] D. A. Ivanov, H. W. Lee and L. S. Levitov, *Coherent states of alternating current*, PRB 56, 6839 (1997). [Author PDF](https://arxiv.org/pdf/cond-mat/9501040), Appendix C finite-charge/noise optimization and Appendix D nonperiodic observation-window discussion read in parsed text. This is the 1995 preprint of the 1997 publication.

[L11] A. V. Lebedev and G. Blatter, *Dynamical Resurrection of the Visibility in a Mach-Zehnder Interferometer*, PRL 107, 076803 (2011). [Author PDF](https://arxiv.org/pdf/1103.4046), main Eqs. (2)–(7), downstream correction geometry, and overlap interpretation read in parsed text. The PDF's regenerated date is not publication date. Requested page-1 screenshot failed; no plot values were used.

[G13] C. Grenier et al., *Fractionalization of minimal excitations in integer quantum Hall edge channels*, PRB 88, 085302 (2013). [Author PDF](https://arxiv.org/pdf/1301.6777), Section III.A.2, Eqs. (20)–(22), correction reference 67, and the stated interaction/temperature scope checked. Requested page-6 screenshot failed; no unseen graph supplied a quantitative claim.

[R21] B. Roussel, C. Cabart, G. Feve and P. Degiovanni, *Processing Quantum Signals Carried by Electrical Currents*, PRX Quantum 2, 020314 (2021). [Publisher PDF](https://journals.aps.org/prxquantum/pdf/10.1103/PRXQuantum.2.020314), introduction, excitation decomposition, and Section V.A.2 source/entropy optimization read in parsed text. Requested screenshots failed; figure/table numbers are not used to support the comparison.

[C18] C. Cabart, B. Roussel, G. Feve and P. Degiovanni, *Taming electronic decoherence in one-dimensional chiral ballistic quantum conductors*, PRB 98, 155302 (2018). [Primary abstract](https://arxiv.org/abs/1804.04054) and publisher metadata only. Full construction remains unread in this pass.

[K06] J. Keeling, I. Klich and L. S. Levitov, *Minimal Excitation States of Electrons in One-Dimensional Wires*, PRL 97, 116403 (2006). The clean-electron ingredient and prior source reading are retained in scout 08; no new full-paper reading is asserted here.

[D13] J. Dubois et al., *Minimal-excitation states for electron quantum optics using levitons*, Nature 502, 659–663 (2013), [publisher record](https://www.nature.com/articles/nature12713). Abstract-level experimental context only. No preparation fidelity, waveform implementation or energy budget in the present model is assigned to that experiment.
