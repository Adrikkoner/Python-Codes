# Graph both of the following functions on a single figure, with
# a usefully-sized scale.
# (a)x4e−2x
# (b)[x2e−xsin(x2)]2
# Make sure your figure has legend, range, title, axis labels, and so on.

# importing matplotlib module
from matplotlib import pyplot as plt
import numpy as np
from math import pi

x = np.linspace(0, pi, 10000)

ya = np.exp(x)*np.sin(15*x)


# Note that even in the OO-style, we use `.pyplot.figure` to create the figure.
fig, ax = plt.subplots()  # Create a figure and an axes.
ax.plot(x, ya, label="Function")  # Plot some data on the axes.
ax.set_xlabel("x")  # Add an x-label to the axes.
ax.set_ylabel("y")  # Add a y-label to the axes.
ax.set_title("Function plot")  # Add a title to the axes.
ax.legend()  # Add a legend.
plt.hlines(0,0,pi, colors = 'red')
plt.show()
