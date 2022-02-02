from matplotlib import pyplot as plt
import numpy as np
from math import sin


def funcy(x, y, z):
    y1 = z
    return y1


def funcz(x, y, z):
    z1 = -(3 * z + 4 * y)
    return z1


def runge(x0, y0, z0):
    p = []
    q = []
    h = 0.01
    x = np.linspace(0, 1, 1000)
    for x0 in x:
        k1 = funcy(x0, y0, z0)
        k2 = funcy(x0 + h / 2, y0 + ((h / 2) * k1), z0)
        k3 = funcy(x0 + h / 2, y0 + ((h / 2) * k2), z0)
        k4 = funcy(x0 + h, y0 + (h * k1), z0)
        y0 = y0 + (h / 6) * (k1 + (2 * k2) + (2 * k3) + k4)
        p.append(y0)
        k01 = funcz(x0, y0, z0)
        k02 = funcz(x0 + h / 2, y0, z0 + ((h / 2) * k01))
        k03 = funcz(x0 + h / 2, y0, z0 + ((h / 2) * k02))
        k04 = funcz(x0 + h, y0, z0 + (h * k01))
        z0 = z0 + (h / 6) * (k01 + (2 * k02) + (2 * k03) + k04)
        q.append(z0)

    return p, q


x0, y0, z0 = 0, 1, 0
x = np.linspace(0, 1, 1000)
y, z = runge(x0, y0, z0)
y = np.array(y)
z = np.array(z)
# print(y)

fig, ax = plt.subplots()  # Create a figure and an axes.
ax.plot(x, y, label="y")  # Plot some data on the axes.
ax.plot(x, z, label="z")  # Plot some data on the axes.
ax.set_xlabel("x")  # Add an x-label to the axes.
ax.set_ylabel("y")  # Add a y-label to the axes.
ax.set_title("Runge kutta 4th order")  # Add a title to the axes.
ax.legend()  # Add a legend.
plt.show()
