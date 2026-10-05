# Numerical refinement and independent crosscheck

The first seven-group run passed its assertions but emitted scipy IntegrationWarning messages in some very narrow-notch integrations. A tangent substitution compresses smooth off-notch contributions into an endpoint boundary layer; using it for all three integrals was not a reliable final numerical implementation.

The final evaluator subdivides each original-frequency half-cell geometrically at the natural notch width. It keeps the same integrands, test tolerances, endpoints, target fidelities and analytic tail bounds. No warning is suppressed. The final run and its repeat emit no IntegrationWarning, and an independent direct-frequency quadrature checks representative results. The warning-bearing first script and complete output remain in development/check_initial.py and evidence/first_*.

After that numerical refinement, a check using the optimized neutral error waveform itself was added to the existing fermionic-overlap test group. It agrees with the coherent-state fidelity in a finite-circle regularization and approaches the continuum exponent as the frequency spacing is refined. It is not a large-electron simulation or a replacement for the continuum proof.

Both patches are retained. Reversing the crosscheck addition followed by the quadrature refinement recovers the exact initial script; the run record verifies this in an isolated temporary directory. Log timing and terminal-environment text are not claimed byte-identical. No scientific assertion failed in this round.
