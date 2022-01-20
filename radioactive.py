import numpy as np
from scipy.integrate import odeint 
from matplotlib import pyplot as plt

def decayformula(t, N0, lamda):
    return N0*np.exp(-lamda*t)
def derivative(N,t):
    return -lamda*N
# First part
# Calculation of N0
lamda = 0.05
time = 50
N = 821

N0 = N*1.0/np.exp(-lamda*time)
print("Initial number of atoms:", N0)
# Second part
# equation of the system dN/dt = -N
time = np.linspace(0, 100, 10000)
N = odeint(derivative, N0, time)
plt.plot(time, N)
plt.show()