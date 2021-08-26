import numpy as np
from matplotlib import pyplot as plt

x = np.linspace(0, 1, 1000)
yexp1 = np.exp(x ** 0.5)
yexp4 = np.exp(x ** 0.1)
yexp6 = np.exp(x ** 0.33)
yexp = np.exp(x)
yexp2 = np.exp(x * x)
yexp3 = np.exp(x * x * x)
yexp5 = np.exp(x ** 4)
fig, ax = plt.subplots()  # Create a figure and an axes.
ax.plot(x, yexp, label="(x)")  # Plot some data on the axes.
ax.plot(x, yexp2, label="(x2)")  # Plot more data on the axes...
ax.plot(x, yexp3, label="(x3)")
ax.plot(x, yexp1, label="(x0.5)")  # Plot some data on the axes.
ax.plot(x, yexp4, label="(x0.1)")  # Plot more data on the axes...
ax.plot(x, yexp5, label="(x4)")
ax.plot(x, yexp6, label="(x0.33)")
# Plot some data on the axes.
ax.set_xlabel("x")  # Add an x-label to the axes.
ax.set_ylabel("y")  # Add a y-label to the axes.
ax.set_title("Chapter 0 Problem 00")  # Add a title to the axes.
ax.legend()  # Add a legend.
plt.show()
