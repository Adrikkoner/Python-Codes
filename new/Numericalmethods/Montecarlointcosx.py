from random import uniform
from math import cos, pi
import numpy as np
from matplotlib import pyplot as plt


N = 500000  # number of random points in unit cube


def calculatearea(N):

    count = 0  # number of points with in sphere
    for j in range(N):
        point = (uniform(-pi, pi), uniform(-1, 1))
        # print(point)
        if cos(point[0]) <= abs(point[1]):
            if point[1] < 0:
                count -= 1
            else:
                count += 1
        #print(count)
        Answer = pi  * float(count) / float(N)
    return Answer


value = calculatearea(N)
print("The value of integration =", value)
