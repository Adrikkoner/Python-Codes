from math import log
from matplotlib import pyplot as plt
import numpy as np


def function(x):
    y = np.sin(x)
    return y


def funcplot(initial=-10, final=10):
    x = np.linspace(initial, final, 1000)
    x0 = 0 * x
    y = function(x)
    fig, ax = plt.subplots()  # Create a figure and an axes.
    ax.plot(x, y, label="Given function")  # Plot some data on the axes.
    ax.plot(x, x0, label="x = 0 line")  # Plot some data on the axes.
    ax.set_xlabel("x")  # Add an x-label to the axes.
    ax.set_ylabel("y")  # Add a y-label to the axes.
    ax.set_title("Given function")  # Add a title to the axes.
    ax.legend()  # Add a legend.
    plt.show()


def derivative(x):
    y = np.cos(x)
    return y


def seedsgen(initial=-10, final=10):
    seed = []
    i = initial
    while i <= final:
        if function(i) * function(i - 0.1) < 0:
            seed.append(i)
        i += 0.1
    return seed


def newtonrap(plotfunction=True):
    seeds = seedsgen()
    print("The initial seeds are:", seeds, "The number of seeds:", len(seeds))

    for seed in seeds:

        print("Iterations for seed: ", seed)
        acc = 0.00000000001
        x = seed
        i = 0
        while abs(function(x)) > acc:

            h = function(x) / (1.0 * derivative(x))
            x = x - h
            i += 1

        print("Root is: ", x)
        print("Number of iterations: ", i)
        print("----------------------------------------")

    if plotfunction == True:

        funcplot()


newtonrap()
