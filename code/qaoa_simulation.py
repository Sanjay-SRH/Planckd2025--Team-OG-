import numpy as np
import scipy.linalg as la

N_QUBITS = 3
DIM = 2**N_QUBITS
GRAPH_EDGES = [(0, 1), (1, 2), (2, 0)]

I = np.eye(2)
X = np.array([[0, 1], [1, 0]])
Z = np.array([[1, 0], [0, -1]])

def tensor_prod_n(op_list):
    res = op_list[0]
    for op in op_list[1:]:
        res = np.kron(res, op)
    return res

def create_multi_qubit_op(base_op, target_qubit, N):
    ops = [I] * N
    ops[target_qubit] = base_op
    return tensor_prod_n(ops)

def build_cost_hamiltonian(N, edges):
    C = np.zeros((2**N, 2**N), dtype=complex)
    
    for i, j in edges:
        Zi = create_multi_qubit_op(Z, i, N)
        Zj = create_multi_qubit_op(Z, j, N)
        
        C_ij = 0.5 * (np.eye(2**N) - Zi @ Zj)
        C += C_ij
        
    return C

def build_mixer_hamiltonian(N):
    B = np.zeros((2**N, 2**N), dtype=complex)
    for i in range(N):
        B += create_multi_qubit_op(X, i, N)
    return B

def apply_amplitude_damping(rho, p_ad, target_qubit, N):
    
    K0_base = np.array([[1, 0], [0, np.sqrt(1 - p_ad)]])
    K1_base = np.array([[0, np.sqrt(p_ad)], [0, 0]])
    
    K0_ops = [I] * N
    K1_ops = [I] * N
    K0_ops[target_qubit] = K0_base
    K1_ops[target_qubit] = K1_base
    
    K0 = tensor_prod_n(K0_ops)
    K1 = tensor_prod_n(K1_ops)
    
    rho_new = K0 @ rho @ K0.conj().T + K1 @ rho @ K1.conj().T
    return rho_new

def simulate_qaoa_with_noise(C, B, angles, p_ad, depth=1):
    
    gamma, beta = angles[:depth], angles[depth:]
    N = int(np.log2(C.shape[0]))
    
    rho_plus = np.array([[0.5, 0.5], [0.5, 0.5]])
    rho = tensor_prod_n([rho_plus] * N)
    
    U_C_ops = [la.expm(-1j * g * C) for g in gamma]
    U_B_ops = [la.expm(-1j * b * B) for b in beta]

    for p in range(depth):
        
        U_C = U_C_ops[p]
        rho = U_C @ rho @ U_C.conj().T
        
        for i in range(N):
            rho = apply_amplitude_damping(rho, p_ad, i, N)
            
        U_B = U_B_ops[p]
        rho = U_B @ rho @ U_B.conj().T
        
        for i in range(N):
            rho = apply_amplitude_damping(rho, p_ad, i, N)
            
    expected_cut = np.real(np.trace(rho @ C))
    return expected_cut, rho

if __name__ == "__main__":
    
    C_op = build_cost_hamiltonian(N_QUBITS, GRAPH_EDGES)
    B_op = build_mixer_hamiltonian(N_QUBITS)
    
    print("="*40)
    print("PROBLEM 7: QAOA UNDER AMPLITUDE DAMPING")
    print("="*40)
    
    FIXED_ANGLES_P1 = [0.25, 0.10] 
    
    for p_ad in np.linspace(0.0, 0.5, 6):
        expected_cut, _ = simulate_qaoa_with_noise(
            C_op, B_op, FIXED_ANGLES_P1, p_ad, depth=1
        )
        print(f"p_AD={p_ad:.2f} | QAOA p=1 Expected Cut: {expected_cut:.6f}")