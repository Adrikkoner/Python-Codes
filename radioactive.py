import numpy as np
from matplotlib import pyplot as plt
from scipy.integrate import odeint


def decayformula(t, N_0, lamda):
    return N_0 * np.exp(-lamda * t)


def derivative(N, t):
    return -lamda * N


# First part
# Calculation of N0
lamda = 0.05
time = 50
N = 821

N_0 = N * 1.0 / np.exp(-lamda * time)
print("Initial number of atoms:", N_0)
# Second part
# equation of the system dN/dt = -N
time = np.linspace(0, 100, 10000)
N = odeint(derivative, N_0, time)
plt.plot(time, N)
plt.show()
