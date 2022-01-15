from random import uniform
from math import sqrt, pi
import numpy as np
from matplotlib import pyplot as plt
import threading
import time

# Inherting the base class 'Thread'
class AsyncWrite(threading.Thread):
    def __init__(self, dimensions, gamma, filename):

        # calling superclass init
        threading.Thread.__init__(self)
        self.dimensions = dimensions
        self.gamma = gamma
        self.out = filename + ".txt"

    def run(self):

        f = open(self.out, "a")
        f.write(str(self.dimensions) + "\t" + str(self.gamma) + "\n")
        f.close()
        print("Finished background file write to", self.out)


def calculategama(dimensions, N):

    count = 0
    for j in range(N):
        randomnolist = []
        sum = 0
        for k in range(dimensions):
            randomnolist.append(uniform(-1, 1))
        for point in randomnolist:
            sum = sum + point * point
        if sum <= 1:
            count += 1
    Answer = 2 ** dimensions * float(count) / float(N)
    gama = float(Answer) / float(pi)
    print("Gamma =", gama)
    return gama


def Main():
    print("The calculation started at:", time.asctime())
    dimensions = []
    gamma = []

    for i in range(1, 20, 1):

        print("Calculating for dimension:", i)
        dimensions.append(i)
        gamma.append(calculategama(i, 10000000))
        print("Calculations done for gamma =", i)
        background = AsyncWrite(i, gamma[-1], "volumedata")
        background.start()
        background.join()
        print("-------------------------------------------------")

    print("All calculations are done. Saving the plot.")
    xdata = np.array(dimensions)
    ydata = np.array(gamma)
    fig, ax = plt.subplots()  # Create a figure and an axes.
    ax.plot(xdata, ydata, label=" ")  # Plot some data on the axes.
    ax.set_xlabel("Dimensions")  # Add an x-label to the axes.
    ax.set_ylabel("Gama")  # Add a y-label to the axes.
    ax.set_title("Montecarlo")  # Add a title to the axes.
    ax.legend()  # Add a legend.
    # plt.show()
    plt.savefig("alphavsdimensionplot.png")
    print("The calculation ended at", time.asctime())


if __name__ == "__main__":
    Main()
