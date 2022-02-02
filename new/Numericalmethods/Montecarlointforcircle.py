from random import random
from math import sqrt
import numpy as np
from matplotlib import pyplot as plt

# Since the radius is 1, we can leave it out of most calculations.
N = 100000  # number of random points in unit cube


def calculatepi(N):
    all_x = []
    all_y = []
    inside_x = []
    inside_y = []
    count = 0  # number of points with in sphere
    for j in range(N):
        point = (random(), random())
        all_x.append(point[0])
        all_y.append(point[1])
        if point[0] * point[0] + point[1] * point[1]  < 1:
            count = count + 1
            inside_x.append(point[0])
            inside_y.append(point[1])
    Answer = float(count) / float(N)
    # Make sure to use float, otherwise the answer comes out zero!
    # Also note that in this case the volume of our ” known ” volume(the unit
    # cube) is 1 so multiplying by that volume was easy.
    Answer = Answer * 4  # Actual volume is 4 x our test volume.
    # print(
    #    "The volume of a hemisphere of radius 1 is ", Answer, "+/−", 4 * sqrt(N) / float(N)
    # )
    pii =  Answer 
    # print('the value of the pi is',pii)
    return pii,all_x,all_y,inside_x,inside_y


pii = calculatepi(N)
print("The value of pi =", pii[0])
plt.scatter(np.array(pii[1]), np.array(pii[2]))
plt.scatter(np.array(pii[3]), np.array(pii[4]))
plt.show()