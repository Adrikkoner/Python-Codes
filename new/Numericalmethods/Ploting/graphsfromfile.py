import numpy as np
from matplotlib import pyplot as plt

x = []
y = []

with open("myfile.txt", "r") as f:
    words = f.readlines()
    for word in words:
        word = word.split()
        # print(word)
        x.append(float(word[0]))
        y.append(float(word[1]))

# print(x,y)
x = np.array(x)
y = np.array(y)
yexp = np.exp(x)
yexp2 = np.exp(x * x)

fig, ax = plt.subplots()  # Create a figure and an axes.
ax.plot(x, yexp, label="x")  # Plot some data on the axes.
ax.plot(x, yexp2, label="x2")  # Plot more data on the axes...
ax.set_xlabel("x")  # Add an x-label to the axes.
ax.set_ylabel("y")  # Add a y-label to the axes.
ax.set_title("Chapter 0 Problem 00")  # Add a title to the axes.
ax.legend()  # Add a legend.
plt.show()
