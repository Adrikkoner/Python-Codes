from matplotlib import pyplot as plt
import numpy as np

j = float(input("give the value of the j-"))
k = float(input("give the value of the k-"))
a = float(input("give the value of the a-"))
b = float(input("give the value of the b-"))
c = float(input("give the value of the c-"))
d = float(input("give the value of the d-"))


def func1(t, a, b, j):
    x = np.cos(a * t) - np.cos(b * t) ** j
    return x


def func2(t, c, d, k):
    y = np.sin(c * t) - np.sin(d * t) ** k
    return y


t = np.linspace(-np.pi, np.pi, 1000)
x = func1(t, a, b, j)
y = func2(t, c, d, k)
label = (
    "j="
    + str(j)
    + ",k="
    + str(k)
    + ",a="
    + str(a)
    + ",b="
    + str(b)
    + ",c="
    + str(c)
    + ",d="
    + str(d)
)
fig, ax = plt.subplots()  # Create a figure and an axes.
ax.plot(x, y, label=label)  # Plot some data on the axes.
ax.set_xlabel("x")  # Add an x-label to the axes.
ax.set_ylabel("y")  # Add a y-label to the axes.
ax.set_title("Sophisticated function 2")  # Add a title to the axes.
ax.legend()  # Add a legend.
plt.savefig(label + ".png")
# plt.show()
