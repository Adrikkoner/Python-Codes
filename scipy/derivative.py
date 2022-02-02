import numpy as np
from matplotlib import pyplot as plt
from scipy.misc import derivative


def f(x):
    return x ** 2 * np.sin(2 * x) * np.exp(-x)


x = np.linspace(0, 1, 100)
plt.plot(x, f(x))
plt.plot(x, derivative(f, x, dx=1e-6))
plt.plot(x, derivative(f, x, dx=1e-6, n=2))
plt.grid()
plt.show()
