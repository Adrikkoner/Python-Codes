from matplotlib import pyplot as plt
import numpy as np

r = float(input("give the inner circle radius"))
R = float(input("give the outer circle radius"))
d = float(input("the diatance of the point from the center of the inner circle"))


def func1(theta, R, r, d):
    x = ((R - r) * np.cos(theta)) + d * np.cos(theta) * (
        ((R - r) * theta) / r
    )  # the parametric equations for the hyprotrochoids
    return x


def func2(theta, R, r, d):
    y = ((R - r) * np.sin(theta)) - d * np.sin(theta) * (
        ((R - r) * theta) / r
    )  # the parametric equations for the hyprotrochoids
    return y


theta = np.linspace(0, 12 * np.pi, 1000)
x = func1(theta, R, r, d)
y = func2(theta, R, r, d)
fig, ax = plt.subplots()  # Create a figure and an axes.
ax.plot(x, y, label="Butterfly")  # Plot some data on the axes.
ax.set_xlabel("x")  # Add an x-label to the axes.
ax.set_ylabel("y")  # Add a y-label to the axes.
ax.set_title("Butterfly Curve")  # Add a title to the axes.
ax.legend()  # Add a legend.
plt.show()
