from matplotlib import pyplot as plt
import numpy as np

A = float(input("Give the value of amplitude of first wave(A): "))
B = float(input("Give the value of the amplitude second wave(B): "))
wa = float(input("Give the value of the frequency of the frist wave(wa): "))
wb = float(input("give the value of the frequency of the secoend wave(wb): "))
delta = float(input("give the phase difference between two waves: "))


def func(t, wa, A, delta):
    wat = wa * t
    x = A * np.sin(wat + delta)
    return x


t = np.linspace(-np.pi, np.pi, 1000)
x = func(t, wa, A, delta)
y = func(t, wb, B, 0)
fig, ax = plt.subplots()  # Create a figure and an axes.
ax.plot(x, y, label="Liassjuous")  # Plot some data on the axes.
ax.set_xlabel("x")  # Add an x-label to the axes.
ax.set_ylabel("y")  # Add a y-label to the axes.
ax.set_title("Liassjuous Curve")  # Add a title to the axes.
ax.legend()  # Add a legend.
plt.show()
