from matplotlib import pyplot as plt
import numpy as np
from math import sin


def funcy(x, y):
    y1 = sin(x)
    return y1


def runge(x0, y0):
    p = []
    h = 0.1
    x = np.linspace(0, 10, 100)
    for x0 in x:
        k1 = funcy(x0, y0)
        k2 = funcy(x0 + h / 2, y0 + ((h / 2) * k1))
        k3 = funcy(x0 + h / 2, y0 + ((h / 2) * k2))
        k4 = funcy(x0 + h, y0 + (h * k1))
        y0 = y0 + (h / 6) * (k1 + (2 * k2) + (2 * k3) + k4)
        p.append(y0)
    return p


x0, y0 = 0, 0
x = np.linspace(0, 10, 100)
y = np.array(runge(x0, y0))
# print(y)

fig, ax = plt.subplots()  # Create a figure and an axes.
ax.plot(x, y, label="x")  # Plot some data on the axes.
ax.set_xlabel("x")  # Add an x-label to the axes.
ax.set_ylabel("y")  # Add a y-label to the axes.
ax.set_title("Runge kutta 4th order")  # Add a title to the axes.
ax.legend()  # Add a legend.
plt.show()
