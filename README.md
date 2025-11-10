# Planckd2025--Team-OG-
Summary

Problem 0: The Classical Random Walk
Objective: Compute and plot the Root-Mean-Squared (RMS) displacement of a classical random walk (unbiased coin flip, ) as a function of the number of steps (T).
Core Concept: Diffusion. In a classical random walk, the distance traveled grows slowly because movement is stochastic (probabilistic) and tends to cancel itself out. The RMS displacement is proportional to the square root of time:

Problem 1 & 2: The Quantum Random Walk (Standard/Coin-based)
Objective: Simulate the standard Quantum Random Walk (QRW) and analyze its final position distribution and RMS displacement.
Core Concept: Superposition and Interference. Unlike the classical walk, the quantum walk uses a coin qubit in superposition (e.g., ) and a position register in superposition. The key difference is that the RMS displacement grows linearly with time, significantly faster than the classical walk:
This speedup is due to quantum interference, which constructively reinforces paths away from the origin while destructively canceling paths that return to the starting point.

Problem 7: QAOA under Amplitude Damping
Objective: Simulate the Quantum Approximate Optimization Algorithm (QAOA) for the 3-node MaxCut problem under Amplitude Damping noise and quantify how the expected cut value () degrades as the noise probability () increases.
Core Concept: Noisy Quantum Computation (NISQ Era). This problem uses the density matrix ($\rho$) formalism to model the evolution. Amplitude Damping models energy dissipation (a  state).
The key finding is that as  increases, the expected cut  decreases monotonically. This is because the noise destroys the superposition and entanglement created by QAOA, leading to a performance that quickly falls below the classical random guess, illustrating the fragility of shallow quantum algorithms to dissipation.

TEAM DETAILS:
TEAM NAME = Team OG
Member 1 (Captain) = Sanjay Kumar Tamminani
Member 2 = Kimmi Rishi
