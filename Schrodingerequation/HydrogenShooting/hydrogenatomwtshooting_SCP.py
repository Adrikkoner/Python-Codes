# Solving Hydrogen Atom with Python

# Library imports
from scipy import *
from scipy import integrate
from scipy import optimize
from matplotlib import pyplot as plt
import numpy as np
import time


def fprint(data):
    filename = "HydrogenSCP.out"
    with open(filename, "a") as f:
        f.write(data + "\n")
        print(data)


# Schrodinger equation as a function
def Schroed_deriv(y, r, l, En, lamda):
    "Given y=[u,u'] returns dy/dr=[u',u'']"
    (u, up) = y
    return np.array([up, (l * (l + 1) / r ** 2 - 2 * np.exp(-r / lamda) / r - En) * u])


def Shoot(En, R, l, lamda):
    Rb = R[::-1]
    du0 = -1e-5
    ub = integrate.odeint(Schroed_deriv, [0.0, du0], Rb, args=(l, En, lamda))
    ur = ub[:, 0][::-1]
    norm = integrate.simps(ur ** 2, x=R)
    ur *= 1.0 / np.lib.scimath.sqrt(norm)

    ur = ur / R ** l

    f0 = ur[0]
    f1 = ur[1]
    f_at_0 = f0 + (f1 - f0) * (0.0 - R[0]) / (R[1] - R[0])
    return f_at_0


def FindBoundStates(R, l, nmax, Esearch, lamda):
    n = 0
    Ebnd = []
    u0 = Shoot(Esearch[0], R, l, lamda)
    for i in range(1, len(Esearch)):
        u1 = Shoot(Esearch[i], R, l, lamda)
        if u0 * u1 < 0:
            Ebound = optimize.brentq(
                Shoot, Esearch[i - 1], Esearch[i], xtol=1e-16, args=(R, l, lamda)
            )
            Ebnd.append((n + 1, l, Ebound))
            if len(Ebnd) > nmax:
                break
            n += 1
            fprint("Found bound state at E=%14.9f l=%d n=%d" % (Ebound, l, n))

        u0 = u1

    return Ebnd


fprint("Starting Calculations " + time.asctime() + "\n")
t0 = time.time()
for lamda in [10, 20, 50]:
    Esearch = -1.2 / np.arange(1, 20, 0.2) ** 2

    R = np.logspace(-6, 2, 500)

    nmax = 7
    Bnd = []
    for l in range(nmax - 1):
        Bnd += FindBoundStates(R, l, nmax - l, Esearch, lamda)

    Bnd.sort(key=lambda x: x[2])
    Rb = R[::-1]
    du0 = -1e-5
    pqnum = [1, 2, 3]
    azimqnum = ["s", "p", "d"]
    fig, ax = plt.subplots()  # Create a figure and an axes.

    ax.set_xlabel("r")  # Add an x-label to the axes.
    ax.set_ylabel("u(r)")  # Add a y-label to the axes.
    ax.set_title("Eigenvalue Plot")  # Add a title to the axes.

    for n, l, En in Bnd:
        if l == 0 and 0 < n < 4:
            fprint("------------------------------------------------------------------")
            fprint(
                "Ploting for "
                + str(n)
                + azimqnum[l]
                + " with Energy = "
                + str(En)
                + " and lambda = "
                + str(lamda)
            )
            ub = integrate.odeint(Schroed_deriv, [0.0, du0], Rb, args=(l, En, lamda))
            ur = ub[:, 0][::-1]
            norm = integrate.simps(ur ** 2, x=R)
            ur *= 1.0 / np.lib.scimath.sqrt(norm)
            ax.plot(R, ur, label=str(n) + azimqnum[l])
    ax.legend()
    plt.savefig("HydrogenatonEigenvalueslambda=" + str(lamda) + ".png")
    fprint("***************************************")

fprint("Calculations are done." + time.asctime())
fprint("Time taken for calculations " + str(time.time() - t0) + " secs")
