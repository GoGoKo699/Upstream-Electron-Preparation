# Critical check of the fixed frontier

**5 October 2026. Author-side audit of C1–C2, not independent review.**

Base: `2aef91fb235bcd5082d30805d5c4cd53f679b439`, tree
`3defa719131b970c27b7022ab0e97c5addd32acc`. The checked argument is
[Frontier, Sections 1–4](FIDELITY_FRONTIER.md), compared with the preserved
[scout 09](../archive/scouts/scout10/prior/SCOUT_09.md).

**Finding:** the optimizer, all-input bound and asymptotic coefficient survive.
One qualification is necessary: charge one and finite source energy do not
guarantee a finite relative coherent-displacement norm. The already stated
zero-fidelity convention for divergent $D$ must be understood as a regulated
limit, without asserting a common-Fock-space ket for every allowed waveform.
The [change record](../provenance/FRONTIER_AUDIT_CHANGE.md) identifies the exact
effect on the claims. No waveform competitor is removed.

## 1. Equal-charge, squared full-state overlap

Let $u(t)=pv(t)+(1-p)v(t-\tau)$ and $g=u-f$, where
$f(t)=2w/(t^2+w^2)$. Then $g\in L^1\cap L^2$ and $\int g=0$.
The polarity is chosen so that the positive $2\pi$ pulse injects an electron;
a common reversal of the voltage convention changes no norm below.

In the inherited voltage-source model, passive bosonic scattering maps the
two incident coherent displacements to a product of output displacements.
Tracing the unused output therefore adds no mixedness to this preparation.
This is the specific voltage-source statement in G13, Eq. (20) and the
paragraphs following it, not a statement about arbitrary injected electrons.
The relevant [primary passage](https://arxiv.org/html/1301.6777v1#S3.SS1.SSS2)
was reread for this audit.

After applying the inverse target voltage, the relative displacement is, up
to a common polarity sign,

```math
\delta\alpha(\omega)=-\frac{\widehat g(\omega)}{2\pi\sqrt\omega},
\qquad\omega>0.
```

Retain the common charge sector and introduce the same infrared cutoff
$\varepsilon$ in both states. Weyl multiplication contributes only a scalar
phase; its vacuum amplitude has modulus $\exp(-\|\delta\alpha\|^2/2)$.
Consequently its **squared** modulus is

```math
\mathcal F_\varepsilon
=\exp\left[-\frac1{4\pi^2}\int_\varepsilon^\infty
\frac{|H_p(\omega)\widehat v(\omega)-2\pi e^{-w\omega}|^2}{\omega}\,d\omega\right].
```

The ultraviolet integral is finite by Plancherel, since $g\in L^2$.
When $D<\infty$, the relative displacement converges in its one-boson norm
as $\varepsilon\downarrow0$, and the limit is the actual normalized-state
overlap. When $D=\infty$, the regulated overlaps tend to zero; no convergence
to a ket in the target representation is asserted. This specifies the
existing convention $\mathcal F=e^{-D}$ on the entire waveform class.
Different charges remain orthogonal; a cutoff does not license discarding
the charge sector. The two-Lorentzian identity in Frontier Eq. (2) checks the
same squared-overlap normalization directly in the one-electron sector.

### Why the infrared qualification is necessary

Choose a unit of time and $0<\beta\le1/2$. Set

```math
q_\beta(t)=\frac{\beta\,\mathbf1_{t\ge e}}{t(\log t)^{1+\beta}},
\qquad v(t)=2\pi q_\beta(t).
```

This is real, belongs to $L^1\cap L^2$, and has integral $2\pi$.
Write $L=\log(1/\omega)$ for small positive $\omega$. Since $q_\beta$ is
decreasing, integration by parts bounds the oscillatory tail by

```math
\left|\int_{1/\omega}^\infty q_\beta(t)\cos(\omega t)\,dt\right|
\le\frac{2q_\beta(1/\omega)}\omega=2\beta L^{-1-\beta}.
```

The nonnegative integral of $q_\beta(1-\cos\omega t)$ therefore gives
$\operatorname{Re}(1-\widehat q_\beta)\ge L^{-\beta}(1-2\beta/L)$.
Also $|\widehat q_\beta|\le1$, $|H_p-1|\le(1-p)\tau\omega$ and
$|1-e^{-w\omega}|\le w\omega$. Thus, for sufficiently small $\omega$,

```math
\operatorname{Re}\bigl(e^{-w\omega}-H_p\widehat q_\beta\bigr)
\ge\tfrac12[\log(1/\omega)]^{-\beta},\qquad
D\ge\tfrac14\int_0^{\omega_0}
\frac{d\omega}{\omega[\log(1/\omega)]^{2\beta}}=\infty.
```

Neutrality removes the constant charge mismatch, but supplies no rate of
approach at zero frequency. This analytic counterexample corrects the
unqualified ket language; it does not challenge a positive-fidelity optimum.
The distinction between a formal displacement and an implementer in the
usual Fock representation is standard; see the introduction of
[Lill (2025)](https://doi.org/10.1007/s10955-025-03415-y). Only that general
distinction is used here, not its extended-space constructions.

## 2. The constructive optimum is an admissible waveform

Use $x=\omega\tau$, $a=2w/\tau>0$, $h=|H_p|^2$ and
$A_\mu=H_p^*e^{-ax/2}/(h+\mu x)$ for $\mu>0$.
On a neighborhood of zero $h$ is bounded below. On the remaining half-line
$h+\mu x\ge\mu x$. Bounded derivatives of $H_p,h$, together with the
exponential numerator, show that $A_\mu,A_\mu',A_\mu''$ are integrable
on the positive half-line. There is no singularity at a transmission zero.

Extend to $B(x)=A_\mu(x)$ for $x\ge0$ and
$B(x)=\overline{A_\mu(-x)}$ for $x<0$. This is continuous, $B(0)=1$, and
has an integrable piecewise second derivative. More explicitly,

```math
A_\mu'(0+)=-a/2-\mu-i(1-p),\qquad
B'(0+)-B'(0-)=-a-2\mu.
```

The physical inverse is $v_\mu(t)=\tau^{-1}\int_{\mathbb R}
B(x)e^{-ixt/\tau}\,dx$. It is real and bounded because $B\in L^1$.
Integrating by parts on the two half-lines twice, with the finite derivative
jump retained, gives $v_\mu(t)=O(t^{-2})$. Hence $v_\mu\in L^1\cap L^2$.
Fourier inversion now justifies, rather than merely presumes,
$\int v_\mu=\widehat v_\mu(0)=2\pi$.

Moreover $H_pA_\mu-e^{-ax/2}=-\mu x e^{-ax/2}/(h+\mu x)=O(x)$ near
zero, so $D_\mu<\infty$. Every constructed optimum has a genuine target-relative
state vector. No finite temporal support or finite start is inferred from
these estimates. They hold for every fixed $\mu,a>0$ and $p\in[0,1]$;
uniform tail constants as $\mu\downarrow0$ are neither needed nor asserted.

## 3. Completion without subtracting infinities

For $f_a=e^{-ax/2}$ the following identity is pointwise and nonnegative:

```math
\frac{|H_pA-f_a|^2}{x}+\mu|A|^2
=\left(\frac h x+\mu\right)|A-A_\mu|^2
+\frac{\mu e^{-ax}}{h+\mu x}.
```

The last term has finite integral $D_\mu+\mu U_\mu$: it is bounded near
zero and at large $x$ is at most $e^{-ax}/x$. Integrating gives the identity
in the extended nonnegative reals for **every** admitted competitor. For
finite $D[A]$ it reduces to Frontier Eq. (4). If $U[A]\le U_\mu$, then
$D[A]\ge D_\mu$; equality requires $A=A_\mu$ almost everywhere. Competitors
with infinite $D$ cannot improve the positive-fidelity optimum. The proof
does not integrate the divergent terms $|f_a|^2/x$ separately.

Differentiation on compact positive multiplier intervals gives

```math
U_\mu'=-2\int_0^\infty\frac{xhe^{-ax}}{(h+\mu x)^3}\,dx<0,
\qquad D_\mu'=-\mu U_\mu'>0.
```

Dominated convergence gives $U_\mu\to0$ as $\mu\to\infty$ and
$D_\mu\to0$ as $\mu\downarrow0$, using any fixed positive multiplier as
the relevant dominating integrand. Monotone convergence gives
$D_\mu\to\infty$ as $\mu\to\infty$, since its integrand tends to
$e^{-ax}/x$, and $U_\mu\uparrow\int e^{-ax}/h$ as $\mu\downarrow0$.
The latter is infinite at equal splitting and finite otherwise.
Thus every strictly positive finite budget at equal splitting has its unique
optimum; zero energy is only a limit, consistent with fixed charge. At unequal
splitting the branch ends at the exact inverse's finite energy.

## 4. A bound over the entire frequency axis

At $p=1/2$, set $x_k=(2k+1)\pi$ and split $[0,\infty)$ into
$E=[0,\pi/2]$, $J_0=[\pi/2,2\pi]$ and
$J_k=[2k\pi,2(k+1)\pi]$ for $k\ge1$. On every $J_k$, with $s=x-x_k$,

```math
|s|\le\pi,\quad x_k/2\le x\le2x_k,\quad
s^2/\pi^2\le h(x)=\sin^2(s/2)\le s^2/4,\quad
e^{-ax}\le e^{a\pi}e^{-ax_k}.
```

Put $b=\mu x_k$. In particular $h+\mu x\ge(s^2+b)/\pi^2$.
Using the real-line integrals of $s^2/(s^2+b)^2$ and $1/(s^2+b)^2$,
equal to $\pi/(2\sqrt b)$ and $\pi/(2b^{3/2})$, respectively, gives

```math
\sqrt\mu\,U_\mu(J_k)\le\frac{\pi^5e^{a\pi}}8
\frac{e^{-ax_k}}{\sqrt{x_k}},\qquad
\frac{D_\mu(J_k)}{\sqrt\mu}\le\pi^5e^{a\pi}
\frac{e^{-ax_k}}{\sqrt{x_k}}.
```

These bounds are uniform in $k$ and $\mu>0$, and their right sides are
summable for fixed $a>0$. For each fixed $k$, set
$s=2\sqrt{\mu x_k}\,y$. The same estimates supply integrable domination
in $y$, and the two local limits are

```math
\lim_{\mu\downarrow0}\sqrt\mu\,U_\mu(J_k)
=\lim_{\mu\downarrow0}\frac{D_\mu(J_k)}{\sqrt\mu}
=\frac{\pi e^{-ax_k}}{\sqrt{x_k}}.
```

On $E$, $h\ge1/2$, so the two scaled contributions are
$O(\sqrt\mu)$ and $O(\mu^{3/2})$. Dominated convergence over the intervals
therefore proves $\sqrt\mu U_\mu\to B(a)$ and
$D_\mu/\sqrt\mu\to B(a)$ with the original convergent sum $B(a)$.
Global optimality and $R=aU$ yield the original coefficient
$C(a)=aB(a)^2$ and $R_{\min}\sim C(a)/[-\log\mathcal F]$.
This is not uniform in varying target width, nor a finite-notch truncation.

## Disposition and stopping point

C1–C2 retain their equations, admissible optimum and fixed-width asymptote.
The infrared qualification changes the interpretation of divergent-error
competitors only. No scientific reference output or protected source changes.
C3's separate occupied-space/hole argument and C4–C5 were not newly certified
by this audit. Finite-$D$ language in the hole discussion is aligned with the
same domain; its inequality is unchanged.

The three requested implications have now been assessed. This is the stopping
point of the bounded proof task. Independent critical reading, significance
relative to inherited regularized inversion, and physical-premise evidence
remain open; passing this audit resolves none of those questions automatically.
