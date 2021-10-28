# Solving Hydrogen Atom with Python

# Library imports
from scipy import *
from scipy import integrate
from scipy import optimize
from matplotlib import pyplot as plt
import numpy as np
import time

# Modifies print function to write in console and file simultaneously
def fprint(data):
    filename = "HydrogenShootingZvar.out"
    with open(filename, "a") as f:
        f.write(data + "\n")
        print(data)


# Schrodinger equation as a function
def Schroed_deriv(y, r, l, En, Z):
    "Given y=[u,u'] returns dy/dr=[u',u'']"
    (u, up) = y
    return np.array([up, (l * (l + 1) / r ** 2 - 2 * Z / r - En) * u])


# Subroutine to implement shooting method
def Shoot(En, R, l, Z):
    Rb = R[::-1]
    du0 = -1e-5
    ub = integrate.odeint(Schroed_deriv, [0.0, du0], Rb, args=(l, En, Z))
    ur = ub[:, 0][::-1]
    norm = integrate.simps(ur ** 2, x=R)
    ur *= 1.0 / np.lib.scimath.sqrt(norm)

    ur = ur / R ** l

    f0 = ur[0]
    f1 = ur[1]
    f_at_0 = f0 + (f1 - f0) * (0.0 - R[0]) / (R[1] - R[0])
    return f_at_0


# Subroutine to find the Bound state using shooting method
def FindBoundStates(R, l, nmax, Esearch, Z):
    n = 0
    Ebnd = []
    u0 = Shoot(Esearch[0], R, l, Z)
    for i in range(1, len(Esearch)):
        u1 = Shoot(Esearch[i], R, l, Z)
        if u0 * u1 < 0:
            Ebound = optimize.brentq(
                Shoot, Esearch[i - 1], Esearch[i], xtol=1e-16, args=(R, l, Z)
            )
            Ebnd.append((n, l, Ebound))
            if len(Ebnd) > nmax:
                break
            n += 1
            print(
                "Found bound state at E=%14.9f l=%d n=%d"
                % (Ebound, l, n)
            )
        u0 = u1

    return Ebnd


# Starting of calculations

fprint("Starting Calculations " + time.asctime() + "\n")
t0 = time.time()
Esearch = -1.2 / np.arange(1, 20, 0.2) ** 2

R = np.logspace(-6, 1.5, 500)
fig, ax = plt.subplots()  # Create a figure and an axes.
ax.set_xlabel("r")  # Add an x-label to the axes.
ax.set_ylabel("u(r)")  # Add a y-label to the axes.
ax.set_title("Eigenvalue Plot")  # Add a title to the axes.
for Z in [1, 2, 4]:
    nmax = 2
    Bnd = []
    for l in range(nmax - 1):
        Bnd += FindBoundStates(R, l, nmax - l, Esearch, Z)
    Rb = R[::-1]
    du0 = -1e-5
    pqnum = [1, 2, 3]
    azimqnum = ["s", "p", "d"]

    for n, l, En in Bnd:
        if n == 1:
            fprint("------------------------------------------------------------------")
            fprint("Ploting for " + str(n) + azimqnum[l] + " with Energy = " + str(En) + "for Z= " + str(Z))
            ub = integrate.odeint(Schroed_deriv, [0.0, du0], Rb, args=(l, En, Z))
            ur = ub[:, 0][::-1]
            norm = integrate.simps(ur ** 2, x=R)
            ur *= 1.0 / np.lib.scimath.sqrt(norm)
            ax.plot(R, ur, label="Z=" + str(Z) + " " + str(n) + azimqnum[l])
ax.legend()
plt.savefig("HydrogenatonEigenvaluesZvar.png")
fprint("***************************************")

fprint("Calculations are done." + time.asctime())
fprint("Time taken for calculations " + str(time.time() - t0) + " secs")
