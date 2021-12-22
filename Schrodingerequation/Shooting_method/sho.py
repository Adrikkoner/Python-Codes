#potential V(x) = (1/2) m \omega^2 x^2
#\frac{d^2 \psi}{dx^2} = \frac{2m}{\hbar^2}( (1/2) m \omega^2 x^2 -E) \psi
# We set (m \omega/)\hbar =1 and \epsilon = E/\hbar \omega
# \frac{d^2 \psi}{dx^2} = (x^2 - 2\epsilon) 

import numpy as np
from scipy.integrate import odeint, simps
from scipy.optimize import newton
import matplotlib.pyplot as plt

##Function definition
def f(u,x,E):
    f1, f2 = u[1], (x**2 -2*E)*u[0]
    return [f1,f2]

# End of the solution for y for energy E
def shoot(E):
    sol = odeint(f,u,x,args = (E, ))
    return sol[:,0][-1]

#Energy range to explore, x-scale and initial values
energies = np.arange(0,6,0.1)
xmin=-5
xmax=5
x= np.linspace(xmin,xmax,100)
u=[0,0.001]

#locate the eigenenergies from plot

hits = [shoot(E) for E in energies]
plt.plot(energies, hits)
plt.axhline()
plt.show()

#Normalized Eigenfunctions
def psi_normal(En):
    sol=odeint(f,u,x,args=(En, ))
    psi= sol[:,0]
    N = 1/np.sqrt(simps(psi*psi,x))
    return N*psi

#Plot of three eigenfunctions
for n in range(3):
    En = newton(shoot,n)
    print("The energy eigenvalues are {0:.2f}".format(En))
    plt.subplot(1,3,n+1)
    plt.plot(x,psi_normal(En),lw=2)
    plt.title('n={0}'.format(n), size=18)
    plt.axhline(linestyle= '--')

plt.show()
