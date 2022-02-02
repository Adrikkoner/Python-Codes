import numpy as np
from matplotlib import pyplot as plt
from scipy.integrate import odeint, simps
from scipy.optimize import brentq

# import matplotlib as plt


def V(x):
    """
    Potential function in the Harmonic oscillator. Returns V = 0.5 k x^2 if |x|&lt;L and 0.5*k*L^2 otherwise
    """
    if abs(x) < L:
        return lamda * (C * x ** 4 - x ** 2)
    else:
        return lamda * (C * L ** 4 - L ** 2)


def SE(psi, x):
    """
    Returns derivatives for the 1D schrodinger eq.
    Requires global value E to be set somewhere. State0 is first derivative of the
    wave function psi, and state1 is its second derivative.
    """
    state0 = psi[1]
    state1 = (V(x) - E) * psi[0]
    return np.array([state0, state1])


def Wave_function(energy):
    """
    Calculates wave function psi for the given value
    of energy E and returns value at point b
    """
    global psi
    global E
    E = energy
    psi = odeint(SE, psi_init, x)
    return psi[-1, 0]


def find_all_zeroes(x, y):
    """
    Gives all zeroes in y = f(x)
    """
    all_zeroes = []
    s = np.sign(y)
    for i in range(len(y) - 1):
        if s[i] + s[i + 1] == 0:
            zero = brentq(Wave_function, x[i], x[i + 1])
            all_zeroes.append(zero)
    return all_zeroes


N = 1000  # number of points to take on x-axis
psi = np.zeros([N, 2])  # Wave function values and its derivative (psi and psi')
psi_init = np.array([0.001, 0])  # Wave function initial states
E = 0.0  # global variable Energy  needed for Sch.Eq, changed in function "Wave function"
b = 20  # point outside of HO where we need to check if the function diverges
x = np.linspace(
    -b, b, N
)  # x-axis                   # spring constant                      # mass of the body             # classical HO frequency -
h = 1  # normalized Planck constant
L = 15  # size of the HO
lamda = 0.0002
C = 0.045


def main():
    # main program

    en = np.linspace(
        0, lamda * (C * L ** 4 - L ** 2), 1000
    )  # vector of energies where we look for the stable states

    psi_end = []  # vector of wave function at x = b for all of the energies in en
    for e1 in en:
        psi_end.append(
            Wave_function(e1)
        )  # for each energy e1 find the the psi(x) outside of HO

    E_zeroes = find_all_zeroes(en, psi_end)  # now find the energies where psi(b) = 0

    # Plot wave function values at b vs energy vector figure()
    plt.plot(en, psi_end)
    plt.title("Values of the $\Psi(b)$ vs. Energy")
    plt.xlabel("Energy, E")
    plt.ylabel("$\psi(x = b)$")
    for E in E_zeroes:
        plt.plot(E, [0], "go")
        plt.annotate("E = %.2f" % E, xy=(E, 0), xytext=(E, 5))
    plt.grid()
    plt.show()

    # Print energies for the found states
    print("Energies for the bound states are: ")
    for En in E_zeroes:
        print("%.2f " % En)

    # Plot the wave function for 1st 4 eigenstates
    for i in range(4):  # For each of 1st 4 allowed energies
        Wave_function(E_zeroes[i])
        sol = psi[:, 0]
        N = 1 / np.sqrt(simps(sol * sol, x))
        psi_normal = N * sol  # find the wave function psi(x)
        plt.plot(
            x, psi_normal ** 2, label="E = %.2f" % E_zeroes[i]
        )  # and plot it scaled for comparison
    plt.legend()
    plt.title("Wave function")
    plt.xlabel("x, $x/L$")
    plt.ylabel("$|\Psi(x)|^2$", fontsize=10)
    plt.grid()
    plt.show()


if __name__ == "__main__":
    main()
