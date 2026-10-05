# Scout 08: clean-electron synthesis through an interacting two-channel segment

**Decision: one bounded finite-accuracy continuation, not a dedicated PRL project.**

Read `SCOUT_08.md` for the exact model, reachability classification, source-energy
asymptote, countercontrols and novelty boundary. The fractionalization model and
minimal-excitation pulse class are inherited. The present author-side deductions
allow arbitrary finite-energy waveforms in one input, including electron–hole
excitations, rather than only testing an input Lorentzian.

At equal splitting, an exactly hole-free finite output must have even electron
number. The full criterion also constrains its pulse widths and centers. It is
not a prohibition on odd net charge, a universal loss law, or a Cooper-pair effect.
It does not apply to an infinite periodic train, a finite detector time window,
control of both input channels, or a different device Hamiltonian by default.

Away from equal splitting, the exact inverse exists. For a fixed single-electron
Lorentzian target, its energy diverges with the inverse splitting imbalance.
Finite waveform error, electron fidelity, and hole contamination are different
quantities: their operational relation is the next bounded test, not established
by this checkpoint. No hardware or broad usefulness claim is made.

## Reproduce

With Python, NumPy, SciPy and SymPy (versions in `environment.json`):

    python check_pulse_reachability.py --output NEW_REPORT.json

The output must not exist. Six groups check the fermionic excess-coherence kernel,
unitary collective scattering, integer-orbit constructions, a Vandermonde check,
exact inverse-energy formula, and the two-input and delayed-companion controls.
All six groups passed on the first run and on repetition. The JSON reports are
byte-identical; timing/terminal text in the logs is not claimed identical. No
scientific check failed and no formula or tolerance was adjusted for a pass.

The general statements are proved analytically in the note, not inferred from
finite enumeration. All computations are small voltage/Fourier calculations;
there is no many-body Hilbert-space simulation or cloud calculation.

`SOURCES.json` records reading depth. Requested source-PDF screenshots failed;
parsed mathematical text was used, and no unread chart/table values are imported.
The incomplete September-2026 author-listing reference is not upgraded into a
full-paper comparison. No third-party paper or font is redistributed.

`RUN_RECORD.json` pins the four mounted previous-scout files as unchanged context.
No previous scientific code, repository, manuscript, contact list, or project
backlog was used. The departed Stark, transmon, singlet-access, recoil and other
projects remain untouched. The delivered ZIP has a SHA-256 file manifest.
