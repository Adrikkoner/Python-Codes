import numpy as np
from scipy.interpolate import interp1d
from matplotlib import pyplot as plt

x = np.linspace(0, 10, 10)
y = x ** 2 * np.sin(x)
plt.scatter(x, y)

f = interp1d(x, y, kind="cubic")
print(f)
x_dense = np.linspace(0, 10, 100)
y_dense = f(x_dense)
plt.plot(x_dense, y_dense)
plt.show()
