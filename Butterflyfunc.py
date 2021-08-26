from matplotlib import pyplot as plt
import numpy as np


def funcy(t):
    y = np.sin(t) * (np.exp(np.cos(t)) - 2 * np.cos(4 * t) - (np.sin(t / 12)) ** 5)
    return y


def funcx(t):
    x = np.cos(t) * (np.exp(np.cos(t)) - 2 * np.cos(4 * t) - (np.sin(t / 12)) ** 5)
    return x


t = np.linspace(0, 12 * np.pi, 1000)
x = funcx(t)
y = funcy(t)
fig, ax = plt.subplots()  # Create a figure and an axes.
ax.plot(x, y, label="Butterfly")  # Plot some data on the axes.
ax.set_xlabel("x")  # Add an x-label to the axes.
ax.set_ylabel("y")  # Add a y-label to the axes.
ax.set_title("Butterfly Curve")  # Add a title to the axes.
ax.legend()  # Add a legend.
plt.show()
