import numpy as np

Steps = 5

X = np.array([[0, 1], [1, 0]])
C = np.kron(np.eye(2), X)

S = np.array([
    [0, 0, 1, 0],
    [0, 0, 0 ,1],
    [1, 0, 0, 0],
    [0, 1, 0, 0]
])
U_step = S @ C

psi = np.array([1, 0, 0, 0])
path = [0]
for n in range(Steps) :
    psi = U_step @ psi
    if np.isclose(np.abs(psi[1]) + np.abs(psi[3]), 1):
        current_pos = 1
    elif np.isclose(np.abs(psi[0]) + np.abs(psi[2]), 1):
        current_pos = 0
    else:
        current_pos = "Error/Superposition"

    path.append(current_pos)
print(path)