# Calibration and duration of the nominal optimizer

This page evaluates how accurately the equal-mixing energy optimizer must be calibrated and how its energy-weighted duration grows at high fidelity. These are properties of the fixed nominal optimizer, as specified by C5 in the [claim map](MODEL_AND_CLAIMS.md).

## 3. Exact sensitivity of the nominal energy optimizer

The nominal device has p=1/2. Let the actual device have p=1/2+epsilon with the same delay tau, while the voltage remains the pulse designed for nominal equality. This is a deterministic calibration error in an existing parameter, not a new stochastic bath model. No change is made to the target or total input charge.

Set H_0=e^{ix/2}cos(x/2), h=cos^2(x/2), and G=1-e^{ix}. The nominal residual and the parameter derivative obey

```math
H_0A_\mu-f_a=-\frac{\mu x f_a}{h+\mu x}\in\mathbb R,
\qquad
GA_\mu=-\frac{2i\sin(x/2)\cos(x/2)f_a}{h+\mu x}\in i\mathbb R.
```

Their cross term vanishes at every frequency. Therefore, for the entire allowed range |epsilon|<=1/2,

```math
\boxed{D_{\rm actual}(A_\mu)=D_\mu+\epsilon^2K_\mu,\qquad
K_\mu=4\int_0^\infty
\frac{h(1-h)e^{-a x}}{x(h+\mu x)^2}\,dx.}
\tag{1}
```

This is exact in the same model, not a first-order expansion in epsilon. The integral is finite for every mu>0; near zero its integrand is O(x). It quantifies the fidelity of the **fixed nominal optimizer**, not the optimum for the actual asymmetric channel and not a minimax-robust design.

Use $x_k=(2k+1)\pi$ and write $B_0(a)=B(a)$ for the positive sum in [Frontier, Section 4](FIDELITY_FRONTIER.md#4-exact-high-fidelity-cost-at-equal-mixing). Define

```math
B_1(a)=\pi\sum_{k\ge0}\frac{e^{-a x_k}}{x_k^{3/2}}.
```

Near a node x_k+s, h=s^2/4+O(s^4). With c_k=2*sqrt(mu*x_k), the leading term of the K integrand is 16*exp(-a*x_k)*s^2/[x_k*(s^2+c_k^2)^2]. Since the integral of s^2/(s^2+c_k^2)^2 over the line is pi/(2c_k),

```math
K_\mu\sim\frac{4B_1}{\sqrt\mu},\qquad
\boxed{D_\mu K_\mu\longrightarrow4B_0B_1.}
\tag{2}
```

The exponentially decreasing node weights make the residue sum convergent. One can first control finitely many isolated nodes, bound the remaining local contributions by their summable exponential weights, and separate the very large x region, where the exponential beats the inverse powers of mu. The nonsingular near-zero and inter-node contributions are subleading. This is the same fixed-width limit as in the [frontier](FIDELITY_FRONTIER.md).

At fixed a, keeping the calibration penalty negligible relative to the nominal D requires epsilon=o(D) for this optimizer family. A simple finite prescription is

```math
|\epsilon|\le\sqrt{\frac{q D_\mu}{K_\mu}}
\quad\Longrightarrow\quad D_{\rm actual}\le(1+q)D_\mu.
\tag{3}
```

For q=0.1 and a nominal fidelity 0.999, the guaranteed fidelity is 0.999^1.1, approximately 0.9989001. This budget is 10% additional **log infidelity**, not a claim of keeping the final fidelity exactly at the nominal value.

A known nonzero p-1/2 allows a redesigned inverse and removes the exact transmission zeros. Consequently (1)–(3) are not a fundamental assertion that every departure from equal splitting worsens preparation. They are a warning against applying an extremely sharp nominal compensation to an inaccurately calibrated device. For fixed nonzero epsilon, decreasing mu sufficiently far eventually drives D_actual upward, even while the nominal D approaches zero.

## 4. The pulse's energy-weighted duration is also singular

To quantify the long preparation tails, define a normalized source-energy profile proportional to v(t)^2 and its variance

```math
\bar t=\frac{\int t v(t)^2dt}{\int v(t)^2dt},\qquad
\sigma_t^2=\frac{\int(t-\bar t)^2v(t)^2dt}{\int v(t)^2dt}.
```

This is not the charge density of the electron, a detector gate length, or a hard support interval. The existing optimal voltages have sufficiently decaying tails for these moments. In dimensionless form write

```math
A_\mu(x)=e^{-ix/2}b_\mu(x),\quad
b_\mu(x)=\frac{\cos(x/2)e^{-a x/2}}{\cos^2(x/2)+\mu x},\quad x>0,
```

with b extended as a real even function. Parseval's identity gives, relative to the centered target and after removing the common propagation delay,

```math
\boxed{\bar t=-\tau/2,\qquad
\frac{\sigma_t^2}{\tau^2}=\frac{\int_0^\infty|b_\mu'(x)|^2dx}{\int_0^\infty|b_\mu(x)|^2dx}.}
\tag{4}
```

The negative mean time reflects predetermined precompensation, not signaling backward in time. A positive-frequency derivative jump at zero is treated through the continuous, even extension; it does not create a delta function in the first weak derivative.

Near a transmission zero, b is, up to its sign, 2*exp(-a*x_k/2)*s/(s^2+c_k^2). Its derivative is 2*exp(-a*x_k/2)*(c_k^2-s^2)/(s^2+c_k^2)^2. The elementary integral

```math
\int_{-\infty}^\infty\frac{(1-y^2)^2}{(1+y^2)^4}dy=\frac\pi4
```

yields

```math
\int_0^\infty|b_\mu'|^2dx\sim\frac{B_1}{8\mu^{3/2}},\quad
\boxed{\frac{\sigma_t}{\tau}\sim\frac1{\sqrt\mu}\sqrt{\frac{B_1}{8B_0}},
\qquad D_\mu\frac{\sigma_t}{\tau}\to\sqrt{\frac{B_0B_1}{8}}.}
\tag{5}
```

The same isolated-zero/tail argument applies. For an explicit high-frequency tail X, direct differentiation bounds |b'| by exp(-ax/2)*[(1+a)/(2mu*x)+(1/2+mu)/(mu^2*x^2)]. Squaring with (u+v)^2<=2u^2+2v^2 bounds the omitted derivative-norm integral. The independent K tail is at most exp(-aX)/(a*mu*X^2). These analytic omitted-tail bounds accompany the quadrature; floating-point roundoff is not interval-certified.

Equation (5) describes the duration of the unique nominal energy optimizer. Optimizing duration itself, imposing a start time or optimizing robustness defines a different control problem.

## 5. Finite target values and their interpretation

For nominal fidelity 99.9%, refined one-dimensional integrals give:

| Target w/tau | Energy E_in/E_l | Source sigma_t/tau | Absolute p error allowing 10% extra log infidelity |
|---:|---:|---:|---:|
| 1/8 | 213.5436 | 176.0128 | 0.00031774 |
| 1/4 | 71.9086 | 74.4513 | 0.00074761 |
| 1/2 | 6.9435 | 14.0812 | 0.00347647 |
| 1 | 1.1166 | 0.9369 | 0.01855291 |

These p errors are absolute fractions, not relative percentage errors on p. In the first row an actual p=0.501, used with the pulse designed for p=0.500, gives F_actual=0.9980105075. The pulse energy has not changed. Reoptimizing for the known actual p is a different calculation and may improve fidelity.

The broad-target rows are not all in the same high-fidelity asymptotic regime as the short-target row at this particular F; the exact integrals, not Eq. (5) alone, produce the table. All times are expressed relative to the mode-delay difference tau. The source RMS width measures energy spread in time rather than a sharp truncation length.

The bound E_in/E_l>=213.54 for the first row remains an ideal lower bound when extra waveform constraints are imposed under the same dynamics, energy account and fidelity objective. Restricting the allowed waveforms cannot lower that minimum, but may remove attainment by the displayed optimizer. A change in dynamics or coherence requires a separate analysis.

## Sources and provenance

Bracketed source keys resolve in [PRIOR_ART](../literature/PRIOR_ART.md). The preserved [scout 10](../archive/scouts/scout10/SCOUT_10.md) records the derivation and numerical checks.
