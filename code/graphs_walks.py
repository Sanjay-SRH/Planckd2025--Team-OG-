import numpy as np

L = 5
T = 8
Target_V = 3
Dim = L * 2

def create_operators(L):
    H = 1/np.sqrt(2) * np.array([[1, 1], [1, -1]])
    C = np.kron(np.eye(L), H)

    S = np.zeros((Dim, Dim), dtype = complex)
    for x in range (L):
        x_left = (x - 1 + L) % L
        S[2 * x_left + 0, 2 * x + 0] = 1.0

        x_right = (x + 1) % L
        S[2 * x_right + 1, 2 * x + 1] = 1.0

    return C, S
def simulate_qw(L, T):
    C, S = create_operators(L)
    U_step = S @ C

    initial_state = np.zeros(Dim, dtype = complex)
    initial_state[0] = 1 / np.sqrt(2)
    initial_state[1] = 1 / np.sqrt(2)

    final_state = initial_state.copy()
    for t in range(T):
        final_state = U_step @ final_state

    traget_prob = np.abs(final_state[2 * Target_V + 0])**2 + np.abs(final_state[2 * Target_V + 1])**2

    return traget_prob

def simulate_crw(L, T):
    P = np.zeros((L, L))
    prob = 0.5
    for i in range(L):
        P[i, (i - 1 + L) % L] = prob
        P[i, (i + 1) % L] = prob

    initial_dist = np.zeros(L)
    initial_dist[0] = 1.0

    final_dist = initial_dist.copy()
    for t in range (T):
        final_dist = P @ final_dist
    return final_dist[Target_V]

qw_prob = simulate_qw(L, T)
crw_prob = simulate_crw(L, T)

print(f"L = {L}, T = {T}, Target = {Target_V}")
print(f"Quantum Walk Success Probability: {qw_prob}")
print(f"Classical Random Walk Success Probability: {crw_prob}")
