import numpy as np
from scipy.optimize import minimize
from matplotlib import pyplot as plt 
#1st problem
def f(x):
    return (x-3)**2

res = minimize(f, x0=2)
#print(res.x)
x = np.linspace(-10,10,100)
y = f(x)
#plt.plot(x, y)
#plt.scatter(res.x,f(res.x))
#plt.show()

#2nd problem
def f(x):
    return ((x-3)*(x-4))**2

res = minimize(f, x0=1)
print(res.x)
x = np.linspace(0,6,100)
y = f(x)
plt.plot(x, y)
plt.scatter(res.x,f(res.x))
plt.show()

#3rd problem
f = lambda x: (x[0] - 1)**2 + (x[1] - 2.5)**2
cons = ({'type': 'ineq', 'fun': lambda x:  x[0] - 2 * x[1] + 2},
        {'type': 'ineq', 'fun': lambda x: -x[0] - 2 * x[1] + 6},
        {'type': 'ineq', 'fun': lambda x: -x[0] + 2 * x[1] + 2})
bnds = ((0, None), (0, None))
res = minimize(f, (2, 0), bounds=bnds, constraints=cons)
print(res.x)