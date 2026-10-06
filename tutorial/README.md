# Start with one tutorial

**Selected by the author on 6 October 2026.**

The single external learning anchor (source key **FBP16**) is G. Fève, J.-M. Berroir and B. Plaçais,
*Time dependent electronic transport in chiral edge channels*, **Physica E 76,
12–27 (2016)**. Read the [free author-hosted PDF](https://www.phys.ens.psl.eu/~placais/publication/2016_physicaE_Buttiker-in-memoriam_Feve.pdf)
or use the [original article DOI](https://doi.org/10.1016/j.physe.2015.10.006).
The article appeared online in 2015; this is the 2016 volume, not the later
reprint. It is a published pedagogical article, not an arXiv tutorial.

Start with ordinary quantum mechanics, including creation and annihilation
operators, Fourier transforms and basic linear algebra. No prior electron-optics course is assumed. The original
[bridge](BRIDGE.md) supplies the remaining steps into this repository's result;
no second external text is compulsory. The research bibliography records
attribution and evidence, rather than an additional prerequisite list.

## Reading route

| Read in the selected article | Purpose |
|---|---|
| Introduction; Sections 2–4 as needed for circuit terminology | Identify the channel, contact and interaction region. Detailed circuit applications are optional. |
| Section 5, starting on printed p. 19; especially Eqs. (41)–(45) | Follow the two propagation modes and equal-channel scattering matrix. |
| Section 6, starting on printed p. 21 | Connect mode propagation to a pulse splitting in time. |
| Section 7, starting on printed p. 24; especially Eqs. (63)–(70) | Follow voltage preparation through bosonic modes and factorized outgoing coherent states. |
| Section 7, Eqs. (73)–(74) | See a coherent-state overlap calculation; its environmental decoherence factor is not our target fidelity. |

The worked matrix uses equal channels. General mixing, the clean Lorentzian
target, our charge-aware overlap and launched-energy convention are supplied
in the bridge. The article does not contain the constrained frontier.

Notation check: the exponential printed in Eq. (64) omits $\omega$; use the
frequency phases in Eqs. (63) and (68). Our bridge writes the convention
explicitly and does not reproduce that typographical omission.

## From the article to this result

Read [the bridge](BRIDGE.md) in order. It explains why a prescribed electron
and its sea become a weighted spectral error, why energy is a different
quadratic norm, and how their competition gives an attainable minimum.
The scientific endpoint is C1–C2: the all-waveform frontier and its fixed-width
equal-splitting asymptote. The two-contact comparison explains the role of
control access.

| Question after the bridge | Authoritative repository passage |
|---|---|
| What exactly is fixed and optimized? | [Model and claims](../research/MODEL_AND_CLAIMS.md) |
| What are the complete frontier formulas? | [Fidelity frontier](../research/FIDELITY_FRONTIER.md), Sections 1–4 |
| Why is the optimizer an allowed pulse, and why does the infinite sum converge? | [Frontier audit](../research/FRONTIER_AUDIT.md), Sections 2–4 |
| Is the two-contact comparison at the same fidelity? | [Control comparison](../research/CONTROL_COMPARISON.md) |
| Which physical assumptions and earlier results are inherited? | [Assumptions](../literature/ASSUMPTIONS.md) and [control prior art](../literature/CONTROL_PRIOR_ART.md) |

## Check your understanding

Before reading optional supporting results, explain:

1. Why a pure voltage-generated output can still differ from one clean electron.
2. Why the target fixes both an orbital and the rest of the Fermi sea.
3. Why matching total charge is necessary but insufficient for finite relative
   displacement norm.
4. Why the energy budget includes the unobserved output.
5. Why a transfer zero prevents exact inversion but permits every positive error.
6. Why allowing the second contact changes the optimization task.

Answers appear in the bridge and its linked proof passages. HOM contrast is
not substituted for full-state fidelity. C3's separate hole inequality is not
a learning dependency here. The route explains the existing conditional
result; it adds no model, apparatus claim or independent validation.
