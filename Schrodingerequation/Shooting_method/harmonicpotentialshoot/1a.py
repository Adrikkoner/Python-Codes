import numpy as np

rng = np.random.default_rng(seed=42)

ints = rng.random(9)

print(ints)
matrix = ints.reshape(3, 3)
print(matrix)
eigenval, eigenvec = np.linalg.eig(matrix)
print(eigenval, eigenvec)
