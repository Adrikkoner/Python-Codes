import numpy as np
from scipy.integrate import odeint, simps
from scipy.optimize import bisect
import matplotlib.pyplot as plt


def f(u, x, E):
    y, z = u
    f1, f2 = z, (V - E) * y
    return [f1, f2]


# Solution by odeint(), return the end point of y(=\psi)


def shoot(E):
    sol = odeint(f, u, x, args=(E,))
    return sol[:, 0][-1]


# parameters and variables

V = 0
energies = np.arange(0, 200, 0.2)
x = np.linspace(0, 1, 100)
u = [0, 0.001]

# shooting for a range of energy values
hits = [shoot(E) for E in energies]

# plot to locate eigenenergies

plt.plot(energies, hits)
plt.axhline()
plt.show()

# Eigenenergy by roo finding method
En = bisect(shoot, 0, 25)

# eigenfunctions
sol = odeint(f, u, x, args=(En,))
psi = sol[:, 0]

# Normalizd wavefunction

N = 1 / np.sqrt(simps(psi * psi, x))
psi_normal = N * psi

# plot the normalized Eigenfuction
plt.plot(x, psi_normal)
plt.show()
