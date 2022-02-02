from random import uniform
from math import sqrt, pi
import numpy as np
from matplotlib import pyplot as plt
import threading
import time
from mpi4py import MPI
import math

t0 = time.time()

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
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    nprocs = comm.Get_size()
    # number of integration steps
    nsteps = N

    if rank == 0:
        # determine the size of each sub-task
        ave, res = divmod(nsteps, nprocs)
        counts = [ave + 1 if p < res else ave for p in range(nprocs)]

        # determine the starting and ending indices of each sub-task
        starts = [sum(counts[:p]) for p in range(nprocs)]
        ends = [sum(counts[: p + 1]) for p in range(nprocs)]

        # save the starting and ending indices in data
        data = [(starts[p], ends[p]) for p in range(nprocs)]
    else:
        data = None

    data = comm.scatter(data, root=0)
    count = 0
    for j in range(data[0], data[1]):
        randomnolist = []
        sum = 0
        for k in range(dimensions):
            randomnolist.append(uniform(-1, 1))
        for point in randomnolist:
            sum = sum + point * point
        if sum <= 1:
            count += 1
    sum = comm.gather(sum, root=0)
    Answer = 2 ** dimensions * float(count) / float(N)
    gama = float(Answer) / float(pi)
    if rank == 0:
        print("Computed in {:.3f} sec".format(time.time() - t0))
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
