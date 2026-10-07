# One and two inputs at the same fidelity

This supporting corollary of [C1](FIDELITY_FRONTIER.md) and unitarity compares
one and two input contacts at the same target width, center, selected-output
fidelity and launched-edge energy account. The only changed resource is access
to the second voltage contact. Exact two-input preparation costs the target
energy; the derivation below also matches the errors for approximate preparation.

## 1. Control class and reduction

Write $q=1-p$, $z=e^{ix}$ and use the inherited matrix after removing the common
propagation delay,

```math
S_p(x)=\begin{pmatrix}
p+qz&\sqrt{pq}(1-z)\\
\sqrt{pq}(1-z)&q+pz
\end{pmatrix},\qquad S_p^\dagger S_p=I,\quad S_p(0)=I.
```

Allow two deterministic real $L^1\cap L^2$ voltage inputs of charges $(1,0)$.
The auxiliary contact needs no net injected charge. For spectra $A_1,A_2$ let
$(B,C)^T=S_p(A_1,A_2)^T$, with $B$ the selected output and $C$ unrestricted.
Both outputs are again admissible voltage waveforms; the selected charge is one.
Using $a=2w/\tau$, $f_a=e^{-ax/2}$ and target energy $\mathcal E_\ell$,

```math
R_{\rm total}=a\int_0^\infty (|A_1|^2+|A_2|^2)\,dx
=a\int_0^\infty (|B|^2+|C|^2)\,dx,
\qquad D[B]=\int_0^\infty\frac{|B-f_a|^2}{x}\,dx.
```

For every admissible charge-one selected waveform $B$, setting $C=0$ minimizes combined energy and is
attainable by $(A_1,A_2)^T=S_p^\dagger(B,0)^T$. In time, if $b$ is the selected
voltage waveform, this construction is

```math
v_1(t)=p\,b(t)+q\,b(t+\tau),\qquad
v_2(t)=\sqrt{pq}\,[b(t)-b(t+\tau)].
```

Finite sums of translations preserve reality and $L^1\cap L^2$; their integrals
are $(2\pi,0)$. Advances are allowed by the existing whole-line preparation
class. Thus the two-input problem reduces exactly to C1 with $H=1$, not merely
to a relaxation whose optimizer might be inadmissible. The same infrared-limit
convention applies to competitors with divergent $D$.

## 2. Exact matched-fidelity frontier

Fix $0<\mathcal F_0<1$ and $D_0=-\ln\mathcal F_0$. C1 at $H=1$ supplies a unique
$\nu>0$ with

```math
B_\nu(x)=\frac{e^{-ax/2}}{1+\nu x},\qquad
D_0=\int_0^\infty\frac{\nu^2x e^{-ax}}{(1+\nu x)^2}\,dx,
\qquad
R_2(D_0)=a\int_0^\infty\frac{e^{-ax}}{(1+\nu x)^2}\,dx.
```

The admissibility and monotone multiplier coverage are the $p=1$ case of the
[frontier audit](FRONTIER_AUDIT.md), followed by the finite translations above.
$\nu$ is fixed by this two-input error equation and is not the one-input
multiplier. With $y=ax$ and $\lambda=\nu/a$, the same equations become

```math
D_0=\lambda^2\int_0^\infty\frac{y e^{-y}}{(1+\lambda y)^2}\,dy,
\qquad R_2(D_0)=\int_0^\infty\frac{e^{-y}}{(1+\lambda y)^2}\,dy.
```

The normalized two-input frontier depends only on fidelity. This does not make
the physical target energy width independent: $\mathcal E_\ell=\hbar/(2w)$.
For finite positive $D_0$, $0<R_2(D_0)<1$; as $D_0\downarrow0$, dominated
convergence gives $R_2\to1$. Exact preparation has combined energy
$\mathcal E_\ell$, attained by $B=f_a,C=0$.

## 3. Strict one-input penalty and its endpoint

Let $R_1(D_0;p,a)$ be C1's one-input minimum and $A_\mu$ its unique optimizer.
Its selected spectrum $B=H_pA_\mu$ has exactly error $D_0$. Put
$h_p=|H_p|^2$. For $0<p<1$,

```math
R_{\rm unused}
=a\int_0^\infty(1-h_p)|A_\mu|^2\,dx>0.
```

Here $1-h_p=4pq\sin^2(x/2)$ is positive away from a discrete set, and
$A_\mu$ is nonzero almost everywhere. Both factors are bounded on compact
intervals and the total energy is finite. The two-input construction can
reproduce this same $B$ with the unused output set to zero. Consequently,

```math
R_2(D_0)\le R_{\rm selected}(A_\mu)
=R_1(D_0;p,a)-R_{\rm unused}(A_\mu)
<R_1(D_0;p,a),\qquad 0<p<1.
```

For $p=0$ or $1$ there is only a delay or identity, and the frontiers coincide.
At equal splitting and fixed $a>0$, C2 and $R_2\to1$ imply

```math
\frac{R_1(D_0;1/2,a)}{R_2(D_0)}\sim\frac{C(a)}{D_0},
\qquad D_0\downarrow0.
```

Thus restricted control raises the minimum at the same prescribed fidelity;
the singular comparison is not produced by assigning different error targets.
It does not assert $R_1>1$ at every finite error: approximate one-input states
can have energy below the exact target, as the existing table already shows.

## 4. Attribution and limits

Two-input manipulation and eigenmode excitation are established ideas; R20
Section V, Eqs. (40)–(42), is a direct related precedent. This supporting
comparison combines the existing C1 solution with unitarity and does not claim
priority for using a second contact. Source keys resolve in
[PRIOR_ART](../literature/PRIOR_ART.md).

Both budgets count combined launched-edge excess energy in the same ideal
scattering and coherent-state model. Full circuit work and irreversible heat
are different quantities, as specified in the [model](MODEL_AND_CLAIMS.md).
