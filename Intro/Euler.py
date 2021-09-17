from matplotlib import pyplot as plt
import numpy as np
def y(x):
    y=x**2
    return y
x=np.linspace(0,10,100)
x0=0
y0=0   
def euler(x0,y0,x,y):
    u=y0
    h=0.01
    m=100
    fig, ax = plt.subplots()
    for n in range(1,m-1):
        y0=y0+h*y(x(n),y0)
        u=np.linspace(u,y0)
     ax.plot(x, euler(x0,y0,x,y), label= n)  # Plot some data on the axes.
#ax.plot(x, yb, label="(b)")  # Plot more data on the axes...
ax.set_xlabel("x")  # Add an x-label to the axes.
ax.set_ylabel("y")  # Add a y-label to the axes.
ax.set_title("Chapter 0 Problem 00")  # Add a title to the axes.
ax.legend()  # Add a legend.
plt.show()
    