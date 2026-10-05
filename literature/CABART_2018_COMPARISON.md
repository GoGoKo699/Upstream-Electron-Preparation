# Cabart 2018: construction-level comparison

**Recorded 5 October 2026 from the supplied publisher PDF; imported without a new scientific conclusion.**

C. Cabart, B. Roussel, G. Fève and P. Degiovanni, *Taming electronic decoherence in one-dimensional chiral ballistic quantum conductors*, PRB **98**,155302 (2018), [DOI](https://doi.org/10.1103/PhysRevB.98.155302). The source PDF has 28 pages and SHA-256 `6113d031e78a5ed5f0b2015be2742de5ea86640e7d0914edef2c115eda4e5152`. The PDF is not redistributed.

The earlier [readiness record](../archive/readiness/REPOSITORY_HANDOFF.md) distinguishes source-derived statements from our comparison. This pass retains that distinction. Pages 7, 8, 19 and 20 and Figures 6 and 24 were visually checked in the recorded readiness audit. Numerical plots and every appendix derivation were not reimplemented.

## 3. Cabart et al.: source-derived content and the comparison

### 3.1 The open-channel model is inherited directly

Section II.C.3, printed page 155302-7, Eqs. (16)–(17), gives

```math
S_{11}(\omega)=p_+e^{i\omega\tau_+}+p_-e^{i\omega\tau_-},
\qquad p_\pm=(1\pm\cos\theta)/2.
```

After removing the common fast transit delay, setting p=p_- and tau=tau_+-tau_-, it is exactly the candidate transfer H_p. At strong coupling theta=pi/2, the two weights are equal. The model and equal-mode splitting must be attributed as inherited, not presented as a discovery.

### 3.2 Voltage-driven purity is also inherited

Section III.A, printed page 155302-8, describes linear scattering of a product of coherent edge-magnetoplasmon states into another product of coherent states. Appendix A, printed page 155302-20, gives the voltage-to-coherent-displacement relation, with displacement proportional to Vhat/sqrt(omega), together with the Klein charge-shift operator.

Section II.B, printed page 155302-4, distinguishes these pointer-state excitations from general electronic wavepackets, which are superpositions of coherent states and can become entangled with the other channel. The candidate must not claim that its voltage-generated output has undergone irreversible many-body decoherence merely because its single-electron content or overlap with the prescribed target has deteriorated.

The paper supports the ingredients behind the frequency-weighted overlap functional. It does not make that functional or the general coherent-state scattering method a new result of this project.

### 3.3 The paper's principal control changes the sample

Section IV, printed pages 155302-15 through 155302-19, studies passive decoherence control by sample design. Closing the inner channel changes the boundary condition. Section II.C.4, Eq. (21), supplies

```math
t_{\rm loop}(\omega)=S_{11}(\omega)+
\frac{S_{12}(\omega)S_{21}(\omega)}{e^{-i\omega\tau_L}-S_{22}(\omega)}.
```

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


## Present status

The named access gap is closed at this construction level. Independent proof validation, exhaustive priority and an achieved apparatus remain absent. This note does not claim that an arbitrary all-pass inverse satisfies every finite-start/duration constraint; it only identifies the change in the mathematical preparation problem.
