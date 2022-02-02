from random import random
from math import sqrt, sin, pi
import numpy as np
from matplotlib import pyplot as plt

# Since the radius is 1, we can leave it out of most calculations.
N = 10000000  # number of random points in unit cube


def calculatearea(N):

    count = 0  # number of points with in sphere
    for j in range(N):
        point = (random(), 2 * pi * random())
        # print(point)
        if sin(point[1]) ** 2 <= point[0]:
            count = count + 1
    Answer = 2 * pi * float(count) / float(N)
    return Answer


value = calculatearea(1000000)
print("The value of =", value)
