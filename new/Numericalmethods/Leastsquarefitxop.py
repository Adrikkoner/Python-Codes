import numpy as np
from matplotlib import pyplot as plt
from math import log, exp

xdata = []
ydata = []

with open("Numericalmethods\data.txt", "r") as f:

    data = f.readlines()
    for words in data:
        word = words.split()

        xdata.append(float(word[0]))
        ydata.append(float(word[1]))

sumx, sumy, sumxy, sumxx = 0, 0, 0, 0
n = len(xdata)
for i in range(1, n):
    sumx = sumx + log(xdata[i])
    sumy = sumy + log(ydata[i])
    sumxy = sumxy + (log(xdata[i]) * log(ydata[i]))
    sumxx = sumxx + (log(xdata[i]) * log(xdata[i]))
m = (sumxy) / (1.0 * sumxx)
c = (sumy - (m * (sumx))) / (1.0 * n)
A = exp(c)
print("the slope of the curve:", m)
print("Constant:", exp(c))
xdata = np.array(xdata)
ydata = np.array(ydata)
funcx = np.linspace(xdata[0], xdata[-1], 1000)
fig, ax = plt.subplots()  # Create a figure and an axes.
ax.scatter(xdata, ydata, label="Given data")  # Plot some data on the axes.
ax.plot(
    funcx, A * np.exp(m * funcx), label="Fitted Curve"
)  # Plot more data on the axes...
ax.set_xlabel("x")  # Add an x-label to the axes.
ax.set_ylabel("y")  # Add a y-label to the axes.
ax.set_title("Leastsquarefit")  # Add a title to the axes.
ax.legend()  # Add a legend.
plt.show()
