# From interacting edge channels to the preparation frontier

This bridge connects the [selected tutorial](README.md) to the C1–C2 preparation
frontier. The [frontier](../research/FIDELITY_FRONTIER.md) gives the exact formulas;
the [proof audit](../research/FRONTIER_AUDIT.md) supplies the full bounds.

## 1. The physical question

Imagine prescribing one electron's outgoing wavepacket, including an otherwise
undisturbed zero-temperature Fermi sea. You can shape a voltage at one upstream
contact. Before reaching the desired output, the excitation crosses a fixed
region coupling two open channels. How much excess energy must the source
launch to meet a specified fidelity?

Keep the electron's width and center fixed. Allow any deterministic real
voltage of either sign, with one net electron, finite energy and integrable
tails. The second input stays in equilibrium; the second output is free to
carry excitations. There is no finite start, duration or bandwidth constraint.
Propagation is linear, elastic, lossless and dispersionless in the bosonic
description. The bosons here represent collective electron-density waves
(edge magnetoplasmons). These are the premises of the conditional optimization.

## 2. A dictionary and the two-mode transfer

Use the Fourier convention

```math
\widehat v(\omega)=\int_{\mathbb R}e^{i\omega t}v(t)\,dt,
\qquad v(t)=\frac{eV(t)}{\hbar},\qquad
\int_{\mathbb R}v(t)\,dt=2\pi.
```

Here $e>0$ is the elementary-charge magnitude; choose the contact polarity so
this positive pulse adds an electron. A common reversal changes no norm below.

| Quantity in the learning route | Repository notation and meaning |
|---|---|
| Contact voltage | $V(t)$; $v(t)=eV(t)/\hbar$ has units of inverse time. |
| Angular frequency | $\omega$; dimensionless $x=\omega\tau$. |
| Fast and slow flight times | $t_\rho,t_n$; remove $t_\rho$ and set $\tau=t_n-t_\rho>0$. |
| Mode weights in the selected channel | $p,1-p$; squared rotation coefficients, not electron path probabilities. |
| Selected diagonal scattering amplitude | $H_p(x)=p+(1-p)e^{ix}$ after the common delay is removed. |
| Positive-frequency input spectrum | $A(x)=\widehat v(x/\tau)/(2\pi)$. |
| Target width | $w>0$; $a=2w/\tau$. |

The article uses $x$ for position and $a$ for a short-distance cutoff; neither
is the dimensionless variable defined here. Only its ideal, open,
copropagating two-channel model is used, not its dissipative or dispersive
extensions.

The equal-channel matrix in the selected article's Eq. (45) corresponds to
$p=1/2$. The generalization is elementary rotation of the two freely
propagating modes. Set $q=1-p$ and

```math
U_p=\begin{pmatrix}\sqrt p&\sqrt q\\\sqrt q&-\sqrt p\end{pmatrix}.
```

Removing the common propagation phase gives

```math
S_p(x)=U_p\begin{pmatrix}1&0\\0&e^{ix}\end{pmatrix}U_p^T
=\begin{pmatrix}
p+qe^{ix}&\sqrt{pq}(1-e^{ix})\\
\sqrt{pq}(1-e^{ix})&q+pe^{ix}
\end{pmatrix}.
```

Thus $S_p^\dagger S_p=I$ and $S_p(0)=I$. With only the first input driven,
the selected output has spectrum $H_p\widehat v$ and effective voltage

```math
u(t)=p\,v(t)+q\,v(t-\tau).
```

Two delayed contributions can cancel at certain frequencies even though the
full matrix conserves energy. At equal mixing,
$H_{1/2}(x)=e^{ix/2}\cos(x/2)$ vanishes at $x_k=(2k+1)\pi$.
The missing selected-output amplitude goes to the other channel.

## 3. Why the target is exactly one electron plus its sea

The specified Lorentzian voltage is

```math
v_\ell(t)=\frac{2w}{t^2+w^2},\qquad
\widehat v_\ell(\omega)=2\pi e^{-w|\omega|}.
```

Here is the clean-source construction used in the repository (inherited from
K06 in the [reading ledger](../literature/PRIOR_ART.md)). In a linear chiral
channel, a contact voltage multiplies the incoming fermion field by

```math
Q_w(t)=\exp\left[-i\int_{-\infty}^t v_\ell(s)\,ds\right]
=\frac{t+iw}{t-iw},\qquad \frac{Q_w'}{Q_w}=-iv_\ell.
```

Normalize the time-domain field using $e^{-iEt/\hbar}$, with energy measured
from the Fermi level. For the filled sea, $P_0$ projects onto the occupied negative-energy orbitals;
its time-domain kernel is

```math
G_0(t,t')=\langle\psi^\dagger(t')\psi(t)\rangle_0
=\frac{i}{2\pi(t-t'+i0)}.
```

Multiplying by the voltage phases and subtracting the sea gives

```math
\Delta G(t,t')=[Q_w(t)Q_w(t')^*-1]G_0(t,t')
=\frac{w}{\pi(t-iw)(t'+iw)}
=\varphi_w(t)\varphi_w(t')^*,
\qquad \varphi_w(t)=\frac{\sqrt{w/\pi}}{t-iw}.
```

This is one positive rank-one addition to the occupied projector. Its orbital
has support only above the Fermi level: up to a global phase its normalized
energy wavefunction is

```math
\psi_w(E)=\sqrt{\frac{2w}{\hbar}}e^{-wE/\hbar}\mathbf1_{E>0},
\qquad \int_0^\infty|\psi_w(E)|^2dE=1.
```

The exact relation for these phase choices is
$\varphi_w(t)=i(2\pi\hbar)^{-1/2}\int_0^\infty\psi_w(E)e^{-iEt/\hbar}dE$.
The factor $i$ is an irrelevant global phase; the normalizations refer to
$dt$ and $dE$, respectively.

Consequently the occupied projector is $P_0+|\varphi_w\rangle\langle\varphi_w|$:
one electron is added and no occupied sea orbital is removed. This specific
clean-target derivation does not use C3's general hole inequality. The target
energy is

```math
\mathcal E_\ell=\int_0^\infty E|\psi_w(E)|^2dE=\frac{\hbar}{2w}.
```

## 4. Voltage preparation makes the full-state overlap tractable

The selected article's Eqs. (63)–(70) supply the bosonic mode description and
voltage-driven coherent outputs. In the normalization used here, the voltage
displacement at positive angular frequency is

```math
\alpha_v(\omega)=-\frac{e\widehat V(\omega)}{h\sqrt\omega}
=-\frac{\widehat v(\omega)}{2\pi\sqrt\omega},
\qquad h=2\pi\hbar.
```

A coherent displacement describes the electronic many-body state generated
by the voltage, not necessarily a single-electron excitation. A linear
unitary matrix sends a product of coherent inputs to a product of coherent
outputs. The selected voltage-generated output therefore remains pure; a
generic injected electronic wavepacket need not have this property.

For one oscillator, $|\alpha\rangle=D(\alpha)|0\rangle$ and Weyl multiplication
gives $D(\beta)^\dagger D(\alpha)$ as $D(\alpha-\beta)$ times a phase. The
vacuum amplitude of a displacement has modulus $e^{-|\alpha-\beta|^2/2}$.
For a continuum of independent modes, the squared modulus is therefore
$\exp[-\int|\alpha-\beta|^2d\omega]$ whenever the difference is square integrable.

Apply this identity to the **neutral relative displacement** between output
and target. Both have charge one. With a common infrared cutoff,

```math
\mathcal F_\varepsilon=
\exp\left[-\frac1{4\pi^2}\int_\varepsilon^\infty
\frac{|H_p(\omega\tau)\widehat v(\omega)-2\pi e^{-w\omega}|^2}{\omega}\,d\omega\right].
```

Let $\varepsilon\downarrow0$. A finite exponent is the ordinary squared
many-body target overlap. An infinite exponent gives limiting fidelity zero;
it does not assert a state vector in the target representation. Equal charge
removes the constant mismatch at zero frequency but does not ensure convergence.
The [audit](../research/FRONTIER_AUDIT.md#1-equal-charge-squared-full-state-overlap)
gives a counterexample and the precise convention. Individual charged
displacements must not be assigned a vacuum overlap by dropping their charge.

This fidelity asks for the target electron and the correct sea together.
It is not a current-profile match or an HOM contrast. The article's
environmental overlap in Eqs. (73)–(74) illustrates the same mathematical
identity but is a different observable.

## 5. Energy and error weight frequency differently

The excess energy of the incoming coherent modes is

```math
\mathcal E_{\rm in}=\int_0^\infty\hbar\omega|\alpha_v(\omega)|^2d\omega
=\frac{\hbar}{4\pi^2}\int_0^\infty|\widehat v(\omega)|^2d\omega
=\frac{\hbar}{4\pi}\int_{\mathbb R}v(t)^2dt.
```

The last step uses Parseval and reality of $v$, which halves the full
frequency integral. Equivalently this coefficient is $e^2/(2h)$ for $V^2$.
Unitarity makes this incoming excess energy equal to the sum over both outgoing
channels. It is not the full electrical work of the bias circuit or irreversible
heat; the [accounting check](../literature/PREMISE_AUDIT.md#4-energy-convention-and-accounting-check)
fixes that distinction.

In dimensionless variables, set $f_a(x)=e^{-ax/2}$ and $h_p(x)=|H_p(x)|^2$:

```math
D[A]=-\ln\mathcal F[A]=\int_0^\infty\frac{|H_pA-f_a|^2}{x}\,dx,
\qquad U[A]=\int_0^\infty|A|^2dx,
\qquad R[A]=\frac{\mathcal E_{\rm in}}{\mathcal E_\ell}=aU[A].
```

The error penalizes deviation from a fixed output spectrum, weighted by $1/x$.
The energy penalizes the input spectrum. Exact inversion tries $A=f_a/H_p$;
near a simple zero of $H_p$, its energy density behaves as the inverse squared
distance to that zero and is not integrable.

## 6. The best approximate pulse is explicit

For a multiplier $\mu>0$, minimize error plus an energy penalty. Completing
the square at each positive frequency gives

```math
A_\mu(x)=\frac{H_p(x)^*f_a(x)}{h_p(x)+\mu x},
```

```math
\frac{|H_pA-f_a|^2}{x}+\mu|A|^2
=\left(\frac{h_p}{x}+\mu\right)|A-A_\mu|^2
+\frac{\mu e^{-ax}}{h_p+\mu x}.
```

Integrate this nonnegative identity before subtracting constants; it remains
valid for competitors with infinite $D$. It proves that a pulse with energy
no larger than $U[A_\mu]$ cannot have error smaller than $D[A_\mu]$. Conversely,
error no larger than $D[A_\mu]$ requires energy at least $U[A_\mu]$.
Equality on this branch forces $A=A_\mu$ almost everywhere.

This would be only a formal frequency optimum without an admissible inverse.
The [audit](../research/FRONTIER_AUDIT.md#2-the-constructive-optimum-is-an-admissible-waveform)
proves that Hermitian extension gives a real, bounded inverse with
$O(t^{-2})$ tails, integral $2\pi$ and finite $D$. Thus the lower bound is
attained in the stated $L^1\cap L^2$ class. Finite temporal support is not claimed.

The attainable frontier is

```math
R_\mu=a\int_0^\infty\frac{h_p e^{-ax}}{(h_p+\mu x)^2}dx,
\qquad D_\mu=\int_0^\infty\frac{\mu^2xe^{-ax}}{(h_p+\mu x)^2}dx.
```

To require $0<\mathcal F_0<1$, choose the unique $\mu>0$ with
$D_\mu=-\ln\mathcal F_0$. The minimum energy ratio is $R_\mu$. A budget below
it is insufficient; a budget at or above it allows the same attaining pulse,
leaving excess budget unused. At unequal mixing, exact preparation also has
a finite threshold because $h_p$ is bounded away from zero. At equal mixing,
only the perfect endpoint has infinite cost.

## 7. Why the high-fidelity cost diverges

At $p=1/2$, write $x=x_k+s$ near each $x_k=(2k+1)\pi$. Then
$h_{1/2}(x)=s^2/4+O(s^4)$. The denominator balances $s^2$ against $\mu x_k$,
so the important interval has width proportional to $\sqrt{\mu x_k}$.
With $s=2\sqrt{\mu x_k}\,y$, the local energy integral scales as
$\mu^{-1/2}$ and the local error as $\mu^{1/2}$.

Summing the contributions gives

```math
B(a)=\pi\sum_{k\ge0}\frac{e^{-ax_k}}{\sqrt{x_k}},\qquad
R_\mu\sim\frac{aB(a)}{\sqrt\mu},\qquad
D_\mu\sim B(a)\sqrt\mu.
```

This local picture alone does not justify exchanging an infinite sum with a
limit. The [whole-axis bounds](../research/FRONTIER_AUDIT.md#4-a-bound-over-the-entire-frequency-axis)
do that work, including the interval near zero frequency. Eliminating $\mu$
then yields C2:

```math
R_{\min}(\mathcal F;a)\sim\frac{C(a)}{-\ln\mathcal F},
\qquad C(a)=aB(a)^2,\qquad\mathcal F\uparrow1,
```

at **fixed** $a>0$ and equal mixing. The theorem concerns shrinking
neighborhoods of the transfer zeros, not their measure-zero points alone.
Changing target width changes the problem. The asymptote is not a substitute
for the exact finite-error integrals.

## 8. What access to the second contact changes

If both inputs are driven, any admissible charge-one selected waveform $B$ can be produced
with the unused output set to zero by applying $S_p^\dagger(B,0)^T$.
Finite sums of time translations preserve $L^1\cap L^2$ and give incoming
charges $(1,0)$. Counting both inputs' energies reduces the problem to the
identity-transfer case of Section 6.

The [same-fidelity comparison](../research/CONTROL_COMPARISON.md) proves
$R_2(D_0)<R_1(D_0;p,a)$ for every finite $D_0>0$ and $0<p<1$. As
$D_0\downarrow0$, $R_2\to1$; at equal mixing, $R_1\sim C(a)/D_0$.
Two-contact protection is an established idea; the comparison quantifies its
energy advantage for this fixed preparation task.

Along the one-input optimizer, the selected output energy stays at most
$\mathcal E_\ell$ and tends to it at high fidelity. At equal mixing the divergent
energy instead leaves through the unused output. Lossless propagation and a
large restricted-control cost are therefore compatible.

## 9. Where the teaching route ends

You now have the specification, target, state metric, energy norm, constructive
optimum and the reason for the singular endpoint. Read the linked audit for
the complete existence and limit bounds. General reachability and nominal
calibration/duration results are optional supporting material.

These are conditional statements in the fixed ideal model. Additional waveform
restrictions retain its lower bound only if dynamics, energy and fidelity stay
the same. Thermal states, changed dynamics or a different observable require
their own analysis. The [claim map](../research/MODEL_AND_CLAIMS.md) connects each
result to its proof and supporting checks.
