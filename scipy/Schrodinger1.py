from scipy.integrate import odeint
import numpy as np
from matplotlib import pyplot as plt
import scipy.constants as const

def potential(r):
    electron = const.e
    potential = (electron**2)/r**2
    return(potential)

def calc_deri(yvec, r, E = -13.6):
    mh = 1#2*const.electron_mass/(const.hbar**2)
    return (yvec[1], mh*(potential(r)-E))
#E = -13.6
time_vec = np.linspace(-10, 10, 100)
yinit = (1, 1)
yarr = odeint(calc_deri, yinit, time_vec)
print(yarr)

fig, ax = plt.subplots()  # Create a figure and an axes.
ax.plot(time_vec, yarr[:,0], label="(a)")  # Plot some data on the axes.
ax.plot(time_vec, yarr[:,1], label="(b)")  # Plot more data on the axes...
ax.set_xlabel("x")  # Add an x-label to the axes.
ax.set_ylabel("y")  # Add a y-label to the axes.
ax.set_title("Chapter 0 Problem 00")  # Add a title to the axes.
ax.legend()  # Add a legend.
plt.show()