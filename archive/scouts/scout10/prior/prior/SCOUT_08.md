# Single-input synthesis of clean electronic pulses after fractionalization

**5 October 2026. Fresh Merlin–Arthur scout 08.**

**Decision: GO for one bounded finite-accuracy test; no dedicated project or PRL commitment yet.** In an established ideal two-channel model, equal mixing excludes every finite odd-electron, hole-free output from one voltage input, even when the input may contain holes. The admissible even-electron targets admit an explicit classification. Away from equal mixing a single clean electron becomes exactly reachable, but its source-energy cost diverges as mixing approaches equality at fixed target width. These are author-side deductions from inherited electron-optics and linear-scattering ingredients, not a new fractionalization mechanism or an exhaustive priority certificate.

No repository was accessed or modified. Only the four mounted scout-06/07 files were read or hashed as protected context; their content is unchanged. No earlier scientific code, old project work order, manuscript, or external contact is used. This candidate is not a continuation of the Stark pair, recoil-dark-state, backflow, noise-surrogate, or singlet-access problems.

## 1. Three questions screened

| Question | First comparison and action |
|---|---|
| Does coherent motion of emergent monopoles necessarily produce ballistic transport in quantum spin ice? | Stern et al. [I19] explicitly derive quantum diffusion from the spin-configuration constraints in a coherent hopping setting. No distinct unresolved mechanism was isolated. Abstract-level screen only; not a declaration that every spin-ice transport problem is solved. |
| Can a slowly changed local scatterer avoid excitation of a gapless Fermi gas despite orthogonality effects? | Diniz et al. [A25] directly treats a time-dependent localized scattering potential, with related adiabaticity bounds already established [A22]. No distinct parameter regime or theorem was isolated. No calculation or renewed threshold-return problem was selected. |
| Can arbitrary shaping of one voltage input restore a clean electron pulse after two interacting edge modes split its signal? | Selected. The scope is exact state synthesis, not the already established fact that an ordinary input Lorentzian can fractionalize. |

Only the third question received calculations. Its output is a clean finite fermionic excitation above a zero-temperature sea; classical voltage-shape matching alone would not impose its integer-pole constraints.

## 2. Fixed physical model and the meaning of clean

Take two co-propagating integer-quantum-Hall edge channels, initially equilibrium zero-temperature Fermi seas. There is capacitive coupling over a fixed segment, no interchannel electron tunneling, and two lossless dispersionless collective modes. A common transit time is removed. If only input channel 1 is voltage driven, the effective output voltage in that channel is

\[
v_{\rm out}(t)=p\,v(t)+(1-p)v(t-\tau),\qquad 0\le p\le1,\quad\tau>0,
\tag{1}
\]

where v=eV/hbar, with polarity chosen so a positive 2pi pulse injects an electron. The parameter p is the weight of one collective mode; it is not a probability that an individual electron took a path. Equation (1) is the short-range two-channel expression already derived by Grenier et al., Eq. (22) [G13], with p=(1+cos(theta))/2 in their notation.

With Fourier convention vhat(omega)=integral exp(i omega t)v(t)dt,

\[
S_p(\omega)=\begin{pmatrix}p+(1-p)z&\sqrt{p(1-p)}(1-z)\\
\sqrt{p(1-p)}(1-z)&(1-p)+pz\end{pmatrix},\quad
z=e^{i\omega\tau}.
\tag{2}
\]

This matrix is unitary. A voltage drives a coherent displacement of the collective modes. Linear lossless scattering therefore leaves each output in the voltage-generated class; this is an inherited property, not a claim that an arbitrary injected electron state has no many-body decoherence [G13]. The unused input has zero applied voltage. Its output is unrestricted and can carry neutral electron–hole excitations. Neither output is measured or postselected in the construction.

We allow a real input v in L1(R) intersect L2(R), including negative voltage lobes, electron–hole production, and arbitrarily long decaying tails. We do not impose a positive-voltage, single-Lorentzian, fixed-duration, or strict finite-start restriction. Finite source energy in the linear chiral model requires the L2 norm to be finite; the impossibility below already holds without the additional L1 condition.

A **clean N-electron target** has exactly N extra electrons and no holes in the selected outgoing channel, over the full time axis. This is stricter than net charge Ne or one counted electron in a finite detector gate. In the standard regular finite-excitation voltage-source class, minimality gives the finite Lorentzian/Blaschke form [K06,G13]

\[
f(t)=\sum_{j=1}^J m_j L_{w_j}(t-t_j),\qquad
L_w(t)=\frac{2w}{t^2+w^2},\quad w_j>0,\quad m_j\in\mathbb N,
\quad N=\sum_jm_j.
\tag{3}
\]

The corresponding phase is a product of B_j(t)=[t-t_j+iw_j]/[t-t_j-iw_j], each repeated m_j times. This characterization is inherited, not a claim about arbitrary single-electron sources, finite-temperature excess distributions, singular voltage impulses, superconducting contacts, or interacting fractional edges. Smooth finite-rank pure-electron voltage excitations are the declared target class.

One can check their fermionic content directly. For a single factor the excess coherence kernel is

\[
\frac{i}{2\pi}\frac{B(t)\overline{B(s)}-1}{t-s}
=\frac{w}{\pi(t-t_0-iw)(s-t_0+iw)}=\psi(t)\overline{\psi(s)}.
\]

The normalized wavefunction has support only above the Fermi energy. Products telescope into a sum of N positive one-electron kernels with orthonormal dressed orbitals. The checker verifies this independently for selected single and multiple targets. Thus clean here refers to a fermionic state, not merely positive current.

## 3. Equal mixing: no finite-energy synthesis of one clean electron

At p=1/2, the one-input transfer function is

\[
H(\omega)=\frac{1+e^{i\omega\tau}}2
=e^{i\omega\tau/2}\cos(\omega\tau/2).
\]

It has simple zeros at omega_k=(2k+1)pi/tau. If (1) exactly equals f, the unique possible inverse away from those zeros is vhat=fhat/H. For the one-electron target,

\[
\widehat f(\omega)=2\pi e^{-w|\omega|}e^{it_0\omega},
\]

which is nonzero at every finite frequency. Near a transfer zero its squared inverse behaves as a strictly positive constant divided by (omega-omega_k)^2 and is not locally integrable. By Plancherel there is no L2 input.

**This is an arbitrary-input result:** allowing the incoming waveform to create holes or use negative voltage does not fix it. Assigning a value to the inverse at the isolated zero also does not help; the divergence occurs in a neighborhood. The full two-channel dynamics is nevertheless unitary, and finite charge-one input pulses are allowed. Their selected output cannot be an exactly hole-free finite one-electron state in this model.

## 4. Complete classification of finite clean targets at equal mixing

There is a stronger result for every finite target (3). Group its poles by identical width w and by center modulo tau. In one group write t_j=r+n_j tau, with fixed r in [0,tau) and integers n_j. Combine repeated centers into integer multiplicities m_n. Then

\[
\boxed{f\text{ is reachable by a finite-energy one-input voltage at }p=1/2
\iff \sum_n(-1)^n m_n=0\text{ in every such group}.}
\tag{4}
\]

### Necessity

For omega>0 the target transform is a finite exponential sum. L2 solvability requires it to vanish at every omega_k, k>=0. At those zeros it has the form

\[
\frac{\widehat f(\omega_k)}{2\pi}
=\sum_g A_g\lambda_g^k,\quad
\lambda_g=e^{-2\pi w_g/\tau}e^{2\pi i r_g/\tau},\quad
A_g=e^{-\pi w_g/\tau}e^{i\pi r_g/\tau}\sum_n(-1)^n m_{g,n}.
\]

Distinct groups give distinct nonzero lambda_g. The Vandermonde matrix for the first number-of-groups values of k is invertible. Thus vanishing at all transfer zeros forces every A_g to vanish, proving the condition. No numerical scan of a finite frequency band is used in this argument.

### Sufficiency and construction

After shifting each finite integer orbit to start at zero, form F_g(z)=sum_n m_n z^n. The condition is F_g(-1)=0. Division in the integer polynomial ring gives F_g(z)=(1+z)Q_g(z), with finite integer coefficients q_n. Set

\[
v_g(t)=2\sum_n q_n L_{w_g}(t-r_g-n\tau).
\]

It is a finite, smooth L1/L2 waveform and its average with its tau-delayed copy equals the target group exactly. Summing groups proves sufficiency. Some q_n can be negative; the input was expressly allowed to contain holes. The L2 solution is unique because the transfer zeros have measure zero and hence support no nonzero L2 null vector.

### Parity consequence and its exact boundaries

Equation (4) makes the sums of the even- and odd-indexed multiplicities equal in each group. Therefore each group's electron count is even, and so is N:

\[
\boxed{\text{No finite odd-electron, hole-free output can be exactly synthesized
with finite energy from this single input at equal mixing}.}
\tag{5}
\]

Even electron number alone is not sufficient: positions and widths must also obey (4). For example, two pulses of unequal widths fail it. Two equal-width pulses whose centers differ by an odd multiple of tau pass it. For separation 3tau,

\[
v(t)=2[L_w(t)-L_w(t-\tau)+L_w(t-2\tau)]
\quad\mapsto\quad f(t)=L_w(t)+L_w(t-3\tau).
\tag{6}
\]

The incoming waveform is not itself a clean positive pulse. This distinguishes arbitrary-waveform synthesis from merely sending an even-charge Lorentzian through the device. The adjacent-pair special case v=2L_w is already the integer-fractionalization example of G13; neither it nor the existence of even clean output is novel here.

No charge-2e quasiparticle, pairing interaction, or fundamental prohibition of odd charge is implied. Charge is conserved separately at zero frequency, S_p(0)=I. Odd net output charge is possible with additional electron–hole excitations. An infinite periodic train is also outside (3): if its voltage has period tau, (1) just reproduces it, and one clean electron per repetition period is possible. This is consistent with the periodic revivals in G13. The limits of infinite drive duration and finite total electron count must not be conflated.

## 5. Breaking the equality restores exact reachability but costs energy

For p not equal to 1/2,

\[
|H_p(\omega)|\ge d:=|2p-1|>0.
\]

The inverse is bounded on L2. For p>1/2, every target f in (3) has the explicit L1/L2 inverse

\[
v(t)=\frac1p\sum_{n=0}^\infty\left(-\frac{1-p}{p}\right)^n f(t-n\tau).
\tag{7}
\]

Its convergence is absolute in both norms. For p<1/2 the corresponding expansion is advanced: v(t)=[1/(1-p)] sum_{n>=0}[-p/(1-p)]^n f(t+(n+1)tau). Pre-emission is allowed in this whole-line control problem. A real laboratory pulse of finite duration only approximates these waveforms; no finite-start exact-control theorem is implied. For p=0 or 1 there is only a delay or identity.

For a specified single-electron target of width w, the source energy in the chiral linear model is

\[
\mathcal E[v]=\frac{\hbar}{4\pi}\int v(t)^2dt,
\qquad\mathcal E[f]=\frac{\hbar}{2w}.
\]

This follows equally from the current energy density or the inherited collective-mode coherent amplitude [G13, Eq. (20)]. Put a=2w/tau. The unique exact inverse has

\[
\frac{\mathcal E[v]}{\mathcal E[f]}
=a\int_0^\infty\frac{e^{-ax}\,dx}{\cos^2(x/2)+d^2\sin^2(x/2)}.
\tag{8}
\]

Periodic decomposition followed by x=pi+2 arctan(d tan y) gives the nonsingular identity

\[
d\frac{\mathcal E[v]}{\mathcal E[f]}
=\frac{a}{\sinh(\pi a)}\int_{-\pi/2}^{\pi/2}
 e^{-2a\arctan(d\tan y)}dy.
\]

For fixed positive a, dominated convergence yields

\[
\boxed{\frac{\mathcal E[v]}{\mathcal E[f]}
\sim\frac{\pi a}{\sinh(\pi a)}\frac1{|2p-1|}.}
\tag{9}
\]

This cost cannot be reduced by selecting a different exact waveform: the L2 inverse is unique. It is an exact-target statement, not a bound on achievable electron fidelity or hole number at finite error. The source energy also includes excitations emitted into the second channel. Unitarity of (2) implies it equals the sum of both output energies, rather than excess dissipation magically appearing in the interaction region.

For w=tau/2, p=0.505 gives energy ratio about 28.276; p=0.5005 gives about 273.107. The leading coefficient is pi/sinh(pi)=0.272029..., and the divergence is at fixed target duration. Widening the target reduces that coefficient exponentially, so there is no width-independent resource claim or universal finite-accuracy threshold here. These numbers come from one-dimensional quadrature of (8), independently checked against time-domain overlaps of the geometric input train. No many-electron lattice simulation was used.

## 6. Two controls prevent an overstatement

**Control of both inputs removes the restriction.** At equal mixing the two finite waveforms

\[
v_1(t)=\tfrac12[f(t)+f(t+\tau)],\qquad
v_2(t)=\tfrac12[f(t)-f(t+\tau)]
\]

give outputs exactly (f,0). Their combined energy equals that of f. This is the inverse of the full unitary matrix, not a contradiction of the one-driven-input theorem. It requires a second controlled contact and may prepare electron–hole excitations in the input channels. These extra resources were not allowed in (4).

**A finite observation window can hide the compensating pulse.** At equal mixing,

\[
v_N(t)=2\sum_{n=0}^N(-1)^n f(t-n\tau)
\quad\mapsto\quad f(t)-(-1)^{N+1}f(t-(N+1)\tau).
\]

For even N and a one-electron Lorentzian f, this is two clean electrons separated by an arbitrarily long but finite delay. For odd N it is a zero-net-charge electron/hole-type pulse pair, not a hole-free single electron. Increasing the delay can make an early measurement look single-particle while the global output remains different. The theorem does not rule out useful time-gated operation.

## 7. Prior art and the actual Go/No-Go boundary

K06 supplies the analytic minimal-excitation condition; the finite Lorentzian target form is not new. G13 already supplies the full model, the voltage transfer map, interaction-induced electron–hole generation, integer-fractionalization lines for input Lorentzian amplitudes, and periodic revivals. It also explains why long-range dispersion changes those special lines. Our model is a specialization of an established model, not a new transport Hamiltonian.

The attempted increment is explicitly different: allow **any** finite-energy single input, including incoming holes, specify a desired clean output, and classify its attainability. The finite-orbit condition, odd-count prohibition and exact-target energy asymptote were not located as stated results in the inspected primary passages. That is not an exhaustive priority certificate. They use elementary transmission-zero inversion, finite exponential-sum independence and established minimal-pulse theory; a specialist may regard them as a useful but incremental control corollary. That is the principal significance risk.

A 2025 experiment on electron-channel blockade [B25] changes the circuit/mode structure to suppress spreading. That is not the fixed one-port inverse considered here; it also shows that practical alternatives exist. No claim of being the first way to mitigate fractionalization is made. A September 2026 author-listing lead on leviton creation in finite tight-binding chains was found only as an indexed abstract with an incomplete arXiv identifier; it was not used for a theorem comparison or a claimed full reading. No fictitious corrected identifier is supplied.

**Decision: one bounded continuation is justified; a PRL project is not yet selected.** The exact obstruction survives arbitrary input shaping and a finite-charge classification is supplied, so this is more than repeating fractionalization of an unmodified pulse. But perfect preparation at zero temperature can be a fragile target. The next decisive calculation must ask whether the restriction produces a meaningful finite-source-energy bound on the actual outgoing single-electron state fidelity or hole contamination. An L2 error of the voltage alone is not that operational result. A direct check of the closest state-control literature is part of that same decision.

If finite-fidelity operation makes the restriction negligible in the controlled low-energy window, or if an existing control theorem immediately supplies the whole result, checkpoint it instead of adding channels, interactions, topological labels or a new apparatus. No optimization campaign, repository, or manuscript is authorized by this scout. All experimental claims would require independent control of temperature, mode dispersion, drive bandwidth and contact access. The roughly five-to-ten model-matched precedents per load-bearing convention have not been assembled; component citations must not be counted as a demonstrated device.

## 8. Checks and recorded access

Six groups passed on the first run: fermionic minimal kernels and normalized orbitals; full scattering and the spectral obstruction; finite integer-orbit classification/constructions; independent exponential-orbit grouping; exact inverse-energy formulas; and the two-input/delayed-companion controls. The all-finite-target theorem follows from the proof, not enumeration. All numerical work is small Fourier or waveform quadrature; no new symbolic failure, changed equation or relaxed numerical tolerance was needed. Final report reproduction is recorded separately.

The following primary sources were read only to the stated depth. No publication PDF, font or old repository is redistributed. Requested screenshots of the relevant G13 and K06 pages failed; parsed mathematical text was used. No unrendered figure or table values are cited as evidence.

[I19] M. Stern et al., *Quantum percolation of monopole paths and the response of quantum spin ice*, [arXiv:1911.05742](https://arxiv.org/abs/1911.05742). Primary abstract only; coherent diffusion and configuration constraints. No calculation or material choice follows here.

[A25] G. Diniz et al., *Tracking Adiabaticity in Non-Equilibrium Many-Body Systems: The Hard Case of the X-ray Photoemission in Metals*, [arXiv:2502.11313](https://arxiv.org/abs/2502.11313), associated [PRA record](https://journals.aps.org/pra/abstract/10.1103/m17z-4g58). Abstract/model scope only. A close occupied question, not a complete no-go for all local ramps.

[A22] J.-H. Chen and V. Cheianov, *Bounds on quantum adiabaticity in driven many-body systems from generalized orthogonality catastrophe and quantum speed limit*, PRResearch 4,043055 (2022), [primary record](https://journals.aps.org/prresearch/abstract/10.1103/PhysRevResearch.4.043055). Abstract only. Its bounds are not imported into this pulse calculation.

[K06] J. Keeling, I. Klich and L. S. Levitov, *Minimal excitation states of electrons in one-dimensional wires*, PRL 97,116403 (2006), [author PDF](https://arxiv.org/pdf/cond-mat/0604017). Parsed minimal-excitation construction, phase and energy profile, Eqs. (1)–(6). This is the source of the clean voltage-target class, not a new condition claimed here.

[G13] C. Grenier et al., *Fractionalization of minimal excitations in integer quantum Hall edge channels*, PRB 88,085302 (2013), [author PDF](https://arxiv.org/pdf/1301.6777). Parsed Section II clean pulse condition, Section III.B Eqs. (19)–(22), Section IV.A integer-fractionalization discussion and Appendix C coherent-state scattering. No full numerical-figure reproduction or finite-temperature apparatus audit.

[E13] J. Dubois et al., *Minimal-excitation states for electron quantum optics using levitons*, Nature 502,659–663 (2013), [primary article](https://www.nature.com/articles/nature12713). Abstract only: experimental context for voltage-generated clean excitations, not a realization of the proposed inverse waveforms.

[B25] S. Takada et al., *Eigenstate control of plasmon wavepackets with electron-channel blockade*, Nature Communications 16,9942 (2025), [primary article](https://www.nature.com/articles/s41467-025-64876-z). Abstract and introduction only. A distinct circuit intervention, not exact arbitrary waveform synthesis in (1).

[R21] B. Roussel et al., *Processing Quantum Signals Carried by Electrical Currents*, PRX Quantum 2,020314 (2021), [primary abstract](https://journals.aps.org/prxquantum/abstract/10.1103/PRXQuantum.2.020314). Abstract-level state-control lead; no full-paper priority exclusion.
