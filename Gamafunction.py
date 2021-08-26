from matplotlib import pyplot as plt
import numpy as np


def gama(n, x):
    gama = np.exp(-x) * x ** (n - 1)
    return gama


x = np.linspace(0, 10, 1000)

fig, ax = plt.subplots()  # Create a figure and an axes.
for n in range(2, 7):
    ax.plot(x, gama(n, x), label=n)  # Plot some data on the axes.
# ax.plot(x, yb, label="(b)")  # Plot more data on the axes...
ax.set_xlabel("x")  # Add an x-label to the axes.
ax.set_ylabel("y")  # Add a y-label to the axes.
ax.set_title("Chapter 0 Problem 00")  # Add a title to the axes.
ax.legend()  # Add a legend.
plt.show()
