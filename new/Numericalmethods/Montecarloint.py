from random import random
from math import sqrt
import numpy as np
from matplotlib import pyplot as plt

# Since the radius is 1, we can leave it out of most calculations.
N = 10000000  # number of random points in unit cube


def calculatepi(N):

    count = 0  # number of points with in sphere
    for j in range(N):
        point = (random(), random(), random())
        if point[0] * point[0] + point[1] * point[1] + point[2] * point[2] < 1:
            count = count + 1
    Answer = float(count) / float(N)
    # Make sure to use float, otherwise the answer comes out zero!
    # Also note that in this case the volume of our ” known ” volume(the unit
    # cube) is 1 so multiplying by that volume was easy.
    Answer = Answer * 4  # Actual volume is 4 x our test volume.
    # print(
    #    "The volume of a hemisphere of radius 1 is ", Answer, "+/−", 4 * sqrt(N) / float(N)
    # )
    pii = (3 / 4) * Answer * 2

    # print('the value of the pi is',pii)
    return pii


N = []
pii = []

for i in range(100, 1000000, 10000):
    N.append(i)
    pii.append(calculatepi(i))
    print("Calculations done for N =", i)
print("All calculations are done. Starting the plot.")
xdata = np.array(N)
ydata = np.array(pii)
fig, ax = plt.subplots()  # Create a figure and an axes.
ax.plot(xdata, ydata, label=" ")  # Plot some data on the axes.
ax.set_xlabel("x")  # Add an x-label to the axes.
ax.set_ylabel("y")  # Add a y-label to the axes.
ax.set_title("Leastsquarefit")  # Add a title to the axes.
ax.legend()  # Add a legend.
plt.show()
