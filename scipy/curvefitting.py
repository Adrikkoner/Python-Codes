import numpy as np
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit

#Problem 1
x_data = np.linspace(0, 10, 10)
y_data = 5*x_data**2 + 3
plt.scatter(x_data, y_data)


def func(x, a, b):
    return a*x**2 + b

popt, pcov = curve_fit(func, x_data, y_data, p0=(1,1))
a,b = popt
print(a,b)
x_fit = np.linspace(0,10,100)
y_fit = func(x_fit,a,b)
plt.plot(x_fit,y_fit)
plt.show()
#Problem 2
t_data = np.array([ 0.   ,  0.34482759,  0.68965517,  1.03448276,  1.37931034,
        1.72413793,  2.06896552,  2.4137931 ,  2.75862069,  3.10344828,
        3.44827586,  3.79310345,  4.13793103,  4.48275862,  4.82758621,
        5.17241379,  5.51724138,  5.86206897,  6.20689655,  6.55172414,
        6.89655172,  7.24137931,  7.5862069 ,  7.93103448,  8.27586207,
        8.62068966,  8.96551724,  9.31034483,  9.65517241, 10.        ])
y_data = np.array([ 4.3303953 ,  1.61137995, -2.15418696, -3.90137249, -1.67259042,
        2.16884383,  3.86635998,  1.85194506, -1.8489224 , -3.96560495,
       -2.13385255,  1.59425817,  4.06145238,  1.89300594, -1.76870297,
       -4.26791226, -2.46874133,  1.37019912,  4.24945607,  2.27038039,
       -1.50299303, -3.46774049, -2.50845488,  1.20022052,  3.81633703,
        2.91511556, -1.24569189, -3.72716214, -2.54549857,  0.87262548])

plt.plot(t_data,y_data,'*')


def func(x, A, w, phi):
    return A*np.cos(w*x+phi)

popt, pcov = curve_fit(func, t_data, y_data, p0=(4, np.pi, 0))
print(popt)
A, w, phi = popt
print(A,w,phi)
x_fit = np.linspace(0,10,1000)
y_fit = func(x_fit,A, w, phi)
plt.plot(x_fit,y_fit)
plt.show()