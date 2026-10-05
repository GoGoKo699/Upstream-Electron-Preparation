# Upstream electron preparation — repository readiness and the Cabart comparison

**5 October 2026. Recommendation: create a separate, fixed-scope theory repository after the owner authorizes its name, destination and visibility.**

Suggested name: `Upstream-Electron-Preparation`.

This document is an assessment and a handoff, not a newly created repository or a manuscript. No existing repository was read or changed. It uses the delivered scout-10 archive and the newly supplied publisher PDF, *Taming electronic decoherence in one-dimensional chiral ballistic quantum conductors*, C. Cabart, B. Roussel, G. Fève and P. Degiovanni, Physical Review B **98**, 155302 (2018), DOI 10.1103/PhysRevB.98.155302.

## 1. The decision and what the new paper changes

The candidate has moved past scouting: it has a fixed control problem, an analytical energy–fidelity frontier with a matching constructive waveform, an exact-reachability result, explicit hole and source constraints, and runnable checks. Its next useful task is consolidation into a single claim/proof/source map rather than another exploratory extension.

The named Cabart full-text-access gap is now closed at construction level. Its model, bosonization conventions and geometry-based decoherence control have been checked against the candidate. I did not find the constrained upstream energy–many-body-fidelity optimization in those constructions. This conclusion is specific to the supplied paper, not a certificate of global priority or independent confirmation of our proof.

The reading also strengthens a required limitation: **both the available control contact and the propagation geometry are fixed in our theorem.** Merely saying “one upstream contact” is not enough. Cabart et al. obtain a different transmission amplitude by changing the geometry, including closing the otherwise open inner channel. That operation is not allowed in the candidate optimization.

## 2. The fixed research problem

Two open, co-propagating quantum Hall edge channels interact through the lossless, dispersionless two-mode transfer model. The initial electronic reference is the zero-temperature Fermi sea. Only one upstream contact receives a real deterministic voltage; the other input remains in equilibrium. The selected output is compared to one prescribed clean Lorentzian electron plus its Fermi sea, with no accompanying holes. The unused output is unconstrained.

The allowed input class includes integrable, finite-energy waveforms with either sign and arbitrarily long predetermined tails. There is no second driven input, downstream correcting contact, feedback loop, changed sample geometry, finite-start assumption, or thermal-state substitution.

With x=omega*tau, a=2w/tau>0, f_a=exp(-a*x/2), and A=vhat/(2*pi), the current author-side result is

\[
H_p(x)=p+(1-p)e^{ix},\qquad
D[A]=-\ln\mathcal F[A]=\int_0^\infty\frac{|H_pA-f_a|^2}{x}\,dx,
\qquad
R[A]=\frac{\mathcal E_{\rm in}}{\mathcal E_\ell}=a\int_0^\infty|A|^2dx.
\]

At each positive multiplier mu, the optimal waveform is

\[
A_\mu(x)=\frac{H_p(x)^* f_a(x)}{|H_p(x)|^2+\mu x}.
\]

At p=1/2 and fixed target width, the high-fidelity cost is

\[
R_{\min}(\mathcal F;a)\sim\frac{C(a)}{-\ln\mathcal F},\qquad
C(a)=a\left[\pi\sum_{k\ge0}\frac{e^{-a(2k+1)\pi}}{\sqrt{(2k+1)\pi}}\right]^2.
\]

These formulas and their admissible-input argument are claims preserved from scouts 08–10, not assertions taken from the Cabart paper. This pass reruns the existing tests and checks source attribution; it does not present a new independent proof of every earlier claim.

The central physical statement is a resource limit for a **specified state under restricted source control**. It is not a new fractionalization mechanism, a fundamental energy cost of any electron, a state-independent inability to correct propagation, or a measured device performance.

## 3. Cabart et al.: source-derived content and the comparison

### 3.1 The open-channel model is inherited directly

Section II.C.3, printed page 155302-7, Eqs. (16)–(17), gives

\[
S_{11}(\omega)=p_+e^{i\omega\tau_+}+p_-e^{i\omega\tau_-},
\qquad p_\pm=(1\pm\cos\theta)/2.
\]

After removing the common fast transit delay, setting p=p_- and tau=tau_+-tau_-, it is exactly the candidate transfer H_p. At strong coupling theta=pi/2, the two weights are equal. The model and equal-mode splitting must be attributed as inherited, not presented as a discovery.

### 3.2 Voltage-driven purity is also inherited

Section III.A, printed page 155302-8, describes linear scattering of a product of coherent edge-magnetoplasmon states into another product of coherent states. Appendix A, printed page 155302-20, gives the voltage-to-coherent-displacement relation, with displacement proportional to Vhat/sqrt(omega), together with the Klein charge-shift operator.

Section II.B, printed page 155302-4, distinguishes these pointer-state excitations from general electronic wavepackets, which are superpositions of coherent states and can become entangled with the other channel. The candidate must not claim that its voltage-generated output has undergone irreversible many-body decoherence merely because its single-electron content or overlap with the prescribed target has deteriorated.

The paper supports the ingredients behind the frequency-weighted overlap functional. It does not make that functional or the general coherent-state scattering method a new result of this project.

### 3.3 The paper's principal control changes the sample

Section IV, printed pages 155302-15 through 155302-19, studies passive decoherence control by sample design. Closing the inner channel changes the boundary condition. Section II.C.4, Eq. (21), supplies

\[
t_{\rm loop}(\omega)=S_{11}(\omega)+
\frac{S_{12}(\omega)S_{21}(\omega)}{e^{-i\omega\tau_L}-S_{22}(\omega)}.
\]

For its ideal nondissipative model, the paper explicitly states |t_loop|=1. Figure 6 on page 7 distinguishes open and closed geometries. Figure 24 on page 19 depicts the gate that closes the inner edge and compares it with the open configuration. These images were inspected, not inferred solely from a title or abstract.

**Our comparison:** an all-pass response has no real-frequency transmission nulls of the open-channel H_(1/2). Changing H to t_loop therefore changes the constrained preparation problem. The candidate's source-energy divergence must not be described as universal over devices or as a contradiction of the paper's loop protection. No new theorem about admissible inverse-waveform duration in that loop geometry is asserted here.

### 3.4 Their observables are not our global target fidelity

Section II.A.2, pp. 155302-3–4, defines Hong–Ou–Mandel noise in terms of the overlap of excess single-electron Wigner functions. Section III.B uses elastic single-electron scattering amplitudes and inelastic probabilities. Section IV uses these quantities to assess Landau-excitation protection and discusses voltage-driven Leviton fractionalization in the changed geometry.

The candidate optimizes the **full selected-output many-body overlap** with a prescribed clean electron at fixed source energy. An HOM contrast, a first-order coherence, an elastic scattering probability and that global target fidelity must not be silently interchanged. No direct experimental certification of our target fidelity follows from their proposed HOM geometry.

### 3.5 The appendices do not supply the proposed source-energy optimum

The appendix structure was checked: A supplies bosonization; B the single-channel long-range model; C circuit synthesis; D physical constraints on phenomenological velocities; E high-energy decoherence and energy accounting; F low-energy scattering expansions; and G additional sample predictions. In particular, Appendix E's energy integrals concern the energy of injected electrons and interaction-produced electron–hole clouds, not the constrained minimization over arbitrary upstream voltage profiles used here.

This is a construction-level distinction for this paper. It does not establish that no earlier control theorem or another paper could supply the same optimization.

## 4. Important cautions retained from the paper

The model is based on linear electronic dispersion, linear screening and elastic bosonic scattering; the authors explicitly discuss the limits of this framework and dissipation as a separate issue. Their short-range and long-range interaction models can give different coherence predictions. A physical device is not certified by identifying one ideal transfer matrix.

Their discussion on page 15 also notes that sufficiently delayed contributions can overlap excitations from the next source half-period, invalidating an isolated-excitation comparison. That is relevant context for our long preparation tails: the existing isolated-pulse optimum must not be presented as an immediately realizable periodic source. This pass does not derive a repetition-rate bound or import their example's numerical times into our problem.

The newly available paper closes a reading gap. It does not close finite-temperature, bandwidth, finite-start, calibration, detector, or model-matched preparation questions. Nor does it turn the incomplete physical-premise evidence audit into a completed one.

## 5. What the new repository should contain

A short working description is: **“Energy and fidelity limits for preparing a prescribed electron state through a fixed interacting channel with one upstream voltage source.”**

The living research route should be claim-driven rather than chronological:

- `README.md`, `STATUS.md`, `AGENTS.md`, and `work_orders/CURRENT.md`: the physical question, model restrictions, status, verification rules, and one bounded next task.
- `research/MODEL_AND_CLAIMS.md`, `EXACT_REACHABILITY.md`, `FIDELITY_FRONTIER.md`, and `OPTIMIZER_LIMITATIONS.md`: the fixed state/control class, proofs, hole bound, exact controls, and the duration/calibration qualifications. Duration and robustness are properties of the energy optimizer, not general optima.
- `literature/PRIOR_ART.md` and `CABART_2018_COMPARISON.md`: exact attributions, construction-level distinctions, and an honest remaining-reading ledger.
- `checks/` and `results/`: the three existing checker suites, the integral helper, fresh-output run commands and their reference reports. Initial import must distinguish exact byte reproduction from tolerance-based numerical agreement.
- `archive/` and `provenance/`: immutable scouts 08–10, including failed/warning-bearing development attempts and hashes, stored without repeated copies on the main proof route.

No original project, unrelated failed scout, or external publication PDF should be copied into the new repository. Record the Cabart citation and read-depth audit rather than committing the uploaded publisher PDF. Do not infer a license or public/private setting from earlier unrelated repositories.

The first commit should be consolidation plus provenance, not a new extension or a manuscript draft. Preserve the actual proofs and executable checks, not just chat summaries. Replace the active “Cabart abstract-only” label with this audit while retaining the historical scout documents unchanged.

## 6. Initial scope and readiness boundaries

**Repository readiness: yes.** The model and central claim are stable enough to benefit from one versioned record. This is not a decision that all scientific work or priority scrutiny is finished.

**Not yet established:** independent proof confirmation; exhaustive priority; the complete physical-premise audit; finite-temperature or finite-start/bandwidth optimality; a general minimax-robust optimizer; a minimum-duration theorem; a measured preparation or detector protocol.

Do not convert those distinctions into an automatic list of new projects. The next bounded task is to reconcile scouts 08–10 into the model/claim/proof map, attach the C18 comparison, and rerun the existing suites on that exact new tree. Subsequent work should address a concrete objection to the fixed result. Manuscript drafting and outside contact remain uninitiated.

The repository name, account/destination, visibility, license and write/merge authorization have not been selected by this request. The recommendation is `Upstream-Electron-Preparation`; its availability was not checked and no remote resource was created.

## 7. Verification actually performed in this pass

The supplied scout-10 ZIP contains 63 manifest-listed files plus its manifest. Every listed SHA-256 and byte count was verified before and after execution. Its `SCOUT_10.md` is byte-identical to the separately delivered note. The original supplied archive and PDF remain unchanged.

All existing suites were rerun without edits in fresh output paths:

| Existing suite | Groups | Outcome | Report versus its stored reference |
|---|---:|---|---|
| Exact reachability | 6 | PASS | Byte-identical |
| Finite-fidelity frontier | 7 | PASS | Byte-identical |
| Calibration and duration | 5 | PASS | Byte-identical |

These 18 groups are the existing checks, not 18 new research results. No scientific formula, tolerance or reference was changed. Runtime log times are not claimed byte-identical. Numerical integral values remain refined quadrature, not interval-certified roundoff bounds. This is author-side reproducibility, not independent proof review.

The associated `ASSESSMENT_RECORD.json` records source/PDF hashes, each test outcome and exact report comparison. The supplied publisher PDF is 28 pages; the source-transfer, loop-control and bosonization constructions were checked, and pages 7, 8, 19 and 20 were visually inspected. The complete paper's numerical simulations and every appendix derivation were not reimplemented.
