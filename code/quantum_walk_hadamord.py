import numpy as np
import matplotlib.pyplot as plt
import os
N = 50

Pos_Span = 2 * N +1
Hilbert_Dim = 2 * Pos_Span

def create_op(N):
    H = 1/np.sqrt(2) * np.array([[1,1], [1, -1]])
    C = np.kron(np.eye(2 * N +1), H)

    S = np.zeros(((2 * N + 1) * 2, (2 * N + 1) * 2), dtype = complex)

    for x in range (2 * N +1):
        x_prev_0 = x - 1
        x_next_1 = x + 1
        if x_prev_0 >= 0:
            S[2 * x_prev_0 + 0, 2 * x + 0] = 1
        if x_next_1 < 2 * N +1:
            S[2 * x_next_1 + 1, 2 * x + 1] = 1
    return C, S

def evolve(N):
    C, S = create_op(N)
    U_step = S @ C

    initial_state = np.zeros(2 * N * 2 + 2, dtype = complex)
    initial_state[2 * N + 0] = 1.0
    final_state = np.linalg.matrix_power(U_step, N) @ initial_state
    return final_state

def get_probs(final_state, N):
    probabilities = np.zeros(2 * N + 1)

    for x in range (2 * N +1):
        prob_0 = np.abs(final_state[2 * x + 0])**2
        prob_1 = np.abs(final_state[2 * x + 1])**2
        probabilities[x] = prob_0 + prob_1
    return probabilities
final_state = evolve(N)
probabilities = get_probs(final_state, N)

positions = np.arange(-N, N + 1)

plt.figure(figsize = (10, 6))
plt.bar(positions, probabilities, width=1.0, color='purple', alpha=0.7)
plt.title(f'Problem 2: 1D Hadamard Quantum Walk ({N} Steps)')
plt.xlabel('Position (x)')
plt.ylabel('Probability P(x)')
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.xlim(-N, N)

save_path = '../results/hadamard_walk_distribution.png'
os.makedirs(os.path.dirname(save_path), exist_ok = True)
plt.savefig(save_path)

plt.show()