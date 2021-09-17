import numpy as np
from scipy.optimize import root
def func(x):
   return x*4 + 2 * np.cos(x)
sol = root(func, 5)
print(sol.x)

