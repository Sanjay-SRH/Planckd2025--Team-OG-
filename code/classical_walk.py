import numpy as np
import matplotlib.pyplot as plt
import os

MAX_Steps = 1000
NUM_Walks = 5000

def simulate_classical_random_walk():
    steps = np.random.choice([-1, 1], size = (NUM_Walks, MAX_Steps))
    positions = np.cumsum(steps, axis=1)

    initial_positions = np.zeros((NUM_Walks, 1))
    all_positions = np.hstack((initial_positions, positions))

    steps_array = np.arange(MAX_Steps + 1)

    squared_displacements = all_positions*2
    sum_of_squared_displacements = np.sum(squared_displacements, axis=0)

    MSD = sum_of_squared_displacements/NUM_Walks
    RMSD = np.sqrt(MSD)

    return steps_array, RMSD
steps_array, rmsd_values = simulate_classical_random_walk()
theoretical_rmsd = np.sqrt(steps_array)
plt.figure(figsize=(10,6))
plt.plot(steps_array, rmsd_values, label='Simulated RMSD', color='blue', linewidth=2, alpha=0.7)
plt.plot(steps_array, theoretical_rmsd, label=r'Theoretical Scaling: $\sqrt{N}$ (Diffusive)', color='red', linestyle='--', linewidth=1.5)
ballistic_scaling = 0.8*steps_array
plt.plot(steps_array, ballistic_scaling, label=r'Ballistic Scaling: $0(N)$ (For QW Comparision)', color='gray', linestyle=':', linewidth = 1, alpha=0.6)

plt.title('Problem 0: RMS Displacement of 1D Classical Random walk')
plt.xlabel('Number of Steps (N)', fontsize=14)
plt.ylabel(r'Root-Mean-Squared Displacement ($\sigma_{X}$)', fontsize=14)
plt.legend()
plt.grid(True, linestyle='--', alpha=0.5)
plt.ylim(0, np.max(ballistic_scaling) * 1.1)
plt.xlim(0, MAX_Steps)
save_path = '../results/classical_walk_emsd.png'
os.makedirs('results', exist_ok=True)

plt.savefig(save_path)
plt.show()
