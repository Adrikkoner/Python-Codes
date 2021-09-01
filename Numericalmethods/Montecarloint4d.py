from random import  uniform
from math import sqrt, pi
import numpy as np 
from matplotlib import pyplot as plt

# Since the radius is 1, we can leave it out of most calculations.
#N = 10000000  # number of random points in unit cube

def calculategama(dimensions,N):

    count = 0  # number of points with in sphere

    #randomnolist = []
    for j in range(N):
        randomnolist = []
        sum = 0
        for k in range(dimensions):
            randomnolist.append(uniform(-1,1))
            print(randomnolist)
        for point in randomnolist:
            sum = sum + point*point
        if sum < 1:
            count = count + 1

    Answer = float(count) / float(N)
    gama= float(Answer)/float(pi)
    print('Gamma', gama)
    #print('the value of the pi is',pii)
    return gama

dimensions = []
gama = []

for i in range(3,10,1):
    print('Calculating for dimension:',i)
    dimensions.append(i)
    gama.append(calculategama(i,1000000))
    print('Calculations done for gama =',i)

print('All calculations are done. Starting the plot.')
xdata=np.array(dimensions)
ydata=np.array(gama)
fig, ax = plt.subplots()  # Create a figure and an axes.
ax.plot(xdata, ydata, label=" ")  # Plot some data on the axes.
ax.set_xlabel("Dimensions")  # Add an x-label to the axes.
ax.set_ylabel("Gama")  # Add a y-label to the axes.
ax.set_title("Montecarlo")  # Add a title to the axes.
ax.legend()  # Add a legend.
plt.show()




 