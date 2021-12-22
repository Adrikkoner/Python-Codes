#Equation y'' = -y + \frac{2(y')^2}{y} -1 < x<1
#Boundary condition y(-1) = y(1) = \frac{1}{e + e^{-1}} \approx 0.32403
# Exacto solution y(x) = \frac{1}{e^x + e^{-x}}

#We write y'=z = f_1(x,y,z)
# z' = -y +\frac{2z^2}{y}

import numpy as np
from scipy.integrate import odeint

#defining the derivative

def f(u,x):
    y, z, =u
    f1, f2 = z, -y + 2*z**2/y
    return [f1,f2]

x=np.linspace(-1,1,50)
y0= 1/(np.e + 1/np.e)                      #initial value of y
z1, z2 = 0.1,0.3                        #two initial guess values of z


u = [y0,z1]                        #packing with 1st gues value

sol=odeint(f,u,x)
w1=sol[:,0][-1]                         #value of y at eh end point

tol = 0.0001

for i in range(1000):
    u=[y0,z2]                        #packing with 2nd guess value
    sol=odeint(f,u,x)
    w2 = sol[:,0][-1]

    if abs(w1 -w2)< tol:
        break

    z1, z2 =z2,z2+(z2-z1)/(w2-w1)*(y0-w2)
    w1=w2

import matplotlib.pyplot as plt
plt.plot(x, sol[:,0],'o')
plt.plot(x,1/(np.exp(x) + np.exp(-x)))
plt.show()



