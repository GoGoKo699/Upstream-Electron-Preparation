# Cabart 2018: construction-level comparison

C. Cabart, B. Roussel, G. Fève and P. Degiovanni, *Taming electronic decoherence in one-dimensional chiral ballistic quantum conductors*, PRB **98**,155302 (2018), [DOI](https://doi.org/10.1103/PhysRevB.98.155302). The source PDF has 28 pages and SHA-256 `6113d031e78a5ed5f0b2015be2742de5ea86640e7d0914edef2c115eda4e5152`. The PDF is not redistributed.

The comparison uses the publisher text, including visual checks of pages 7,
8, 19 and 20 and Figures 6 and 24. Source statements and the comparison with
the present optimization are distinguished below.

## 1. Source content and comparison

### 1.1 The open-channel model is inherited directly

Section II.C.3, printed page 155302-7, Eqs. (16)–(17), gives

```math
S_{11}(\omega)=p_+e^{i\omega\tau_+}+p_-e^{i\omega\tau_-},
\qquad p_\pm=(1\pm\cos\theta)/2.
```

After removing the common fast transit delay, setting $`p=p_-`$ and
$`\tau=\tau_+-\tau_-`$ gives the transfer $`H_p`$ used here. At strong coupling
$`\theta=\pi/2`$, the weights are equal. The model and equal-mode splitting
are inherited from this description.

### 1.2 Voltage-driven purity is also inherited

Section III.A, printed page 155302-8, describes linear scattering of a product of coherent edge-magnetoplasmon states into another product of coherent states. Appendix A, printed page 155302-20, gives the voltage-to-coherent-displacement relation, with displacement proportional to $`\widehat V(\omega)/\sqrt{\omega}`$, together with the Klein charge-shift operator.

Section II.B, printed page 155302-4, distinguishes these pointer-state excitations from general electronic wavepackets, which are superpositions of coherent states and can become entangled with the other channel. A voltage-generated output can therefore remain pure while its single-electron content or overlap with the prescribed target deteriorates.

These coherent-state ingredients underlie the frequency-weighted overlap functional in the [frontier](../research/FIDELITY_FRONTIER.md).

### 1.3 The paper's principal control changes the sample

Section IV, printed pages 155302-15 through 155302-19, studies passive decoherence control by sample design. Closing the inner channel changes the boundary condition. Section II.C.4, Eq. (21), supplies

```math
t_{\rm loop}(\omega)=S_{11}(\omega)+
\frac{S_{12}(\omega)S_{21}(\omega)}{e^{-i\omega\tau_L}-S_{22}(\omega)}.
```

For its ideal nondissipative model, the paper explicitly states $`|t_{\rm loop}|=1`$. Figure 6 on page 7 distinguishes open and closed geometries. Figure 24 on page 19 depicts the gate that closes the inner edge and compares it with the open configuration.

**Our comparison:** the all-pass response removes the real-frequency transmission
nulls of the open-channel $`H_{1/2}`$. Replacing $`H_p`$ with $`t_{\rm loop}`$ changes
the constrained preparation problem. The source-energy divergence derived for
the open geometry is consistent with protection in the loop geometry; finite-start
or duration requirements on the loop inverse would constitute a separate problem.

### 1.4 Their observables are not our global target fidelity

Section II.A.2, pp. 155302-3–4, defines Hong–Ou–Mandel noise in terms of the overlap of excess single-electron Wigner functions. Section III.B uses elastic single-electron scattering amplitudes and inelastic probabilities. Section IV uses these quantities to assess Landau-excitation protection and discusses voltage-driven Leviton fractionalization in the changed geometry.

This repository optimizes the **full selected-output many-body overlap** with a prescribed clean electron at fixed source energy. HOM contrast, first-order coherence and elastic scattering probability assess different observables from that global target fidelity.

### 1.5 Energy accounting and optimization

The appendix structure was checked: A supplies bosonization; B the single-channel long-range model; C circuit synthesis; D physical constraints on phenomenological velocities; E high-energy decoherence and energy accounting; F low-energy scattering expansions; and G additional sample predictions. In particular, Appendix E's energy integrals concern the energy of injected electrons and interaction-produced electron–hole clouds, not the constrained minimization over arbitrary upstream voltage profiles used here.

## 2. Physical scope

The model is based on linear electronic dispersion, linear screening and elastic bosonic scattering; the authors explicitly discuss the limits of this framework and dissipation as a separate issue. Their short-range and long-range interaction models can give different coherence predictions. Applying the ideal transfer to a physical device requires agreement over the relevant pulse spectrum.

Their discussion on page 15 also notes that sufficiently delayed contributions can overlap excitations from the next source half-period, invalidating an isolated-excitation comparison. That is relevant context for our long preparation tails: the existing isolated-pulse optimum must not be presented as an immediately realizable periodic source. Its example times belong to that paper's source and geometry.

The [premise audit](PREMISE_AUDIT.md) places these source-specific qualifications
alongside the experimental ingredients, and the [control comparison](CONTROL_PRIOR_ART.md)
relates the loop mechanism to other correction and precompensation strategies.
