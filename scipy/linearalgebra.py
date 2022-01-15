import numpy as np
from scipy.linalg import solve

a = np.array([[3, 0, 0, 0], [2, 1, 0, 0], [1, 0, 1, 0], [1, 1, 1, 1]])
b = np.array([4, 2, 4, 2])
x, y, w, z = solve(a, b)
print(x, y, w, z)
