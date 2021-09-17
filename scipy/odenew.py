import numpy as np
from scipy.integrate import odeint
from matplotlib import pyplot as plt
def dvdt(v, t):
    return 3*v**2 - 5
v0 = 0

t = np.linspace(0, 1, 100)
sol = odeint(dvdt, v0, t)
#plt.plot(t,sol)
#plt.show()

def dSdx(S, x):
    y1, y2 = S
    return [y1 + y2**2  + 3*x,
           3*y1 + y2**3 - np.cos(x)]
y1_0 = 0
y2_0 = 0
S_0 = (y1_0, y2_0)
x = np.linspace(0, 1, 100)
sol = odeint(dSdx, S_0, x)


y1_sol = sol.T[0]
y2_sol = sol.T[1]

#plt.plot(x, y1_sol)
#plt.plot(x, y2_sol)
#plt.show()

def dSdt(S, t):
    theta, omega = S
    return [omega,
           np.sin(theta)]
theta0 = np.pi/4
omega0 = 0
S0 = (theta0, omega0)
t = np.linspace(0, 20, 100)
sol = odeint(dSdt, S0, t)
theta, omega = sol.T


plt.plot(t, theta)
plt.show()

