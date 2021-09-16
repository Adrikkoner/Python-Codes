import numpy as np
from scipy.interpolate import interp1d
from matplotlib import pyplot as plt

x = np.linspace(0, 10, 10)
y = x**2 * np.sin(x)
plt.scatter(x,y)
plt.show()