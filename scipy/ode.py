from scipy.integrate import odeint
import numpy as np
from matplotlib import pyplot as plt


def calc_derivative(ypos, time):
    return -2 * ypos


time_vec = np.linspace(0, 4, 40)
y = odeint(calc_derivative, y0=1, t=time_vec)
print(y)

mass = 0.5  # kg
kspring = 4  # N/m
cviscous = 0.4  # N s/m

eps = cviscous / (2 * mass * np.sqrt(kspring / mass))
omega = np.sqrt(kspring / mass)


def calc_deri(yvec, time, eps, omega):
    return (yvec[1], -2.0 * eps * omega * yvec[1] - omega ** 2 * yvec[0])


time_vec = np.linspace(0, 10, 100)
yinit = (1, 0)
yarr = odeint(calc_deri, yinit, time_vec, args=(eps, omega))
print(yarr)

fig, ax = plt.subplots()  # Create a figure and an axes.
ax.plot(time_vec, yarr[:, 0], label="(a)")  # Plot some data on the axes.
ax.plot(time_vec, yarr[:, 1], label="(b)")  # Plot more data on the axes...
ax.set_xlabel("x")  # Add an x-label to the axes.
ax.set_ylabel("y")  # Add a y-label to the axes.
ax.set_title("Chapter 0 Problem 00")  # Add a title to the axes.
ax.legend()  # Add a legend.
plt.show()
