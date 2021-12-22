from numpy import pi
from scipy import constants as const
print('Some values of physical constants')
print('Value of pi',const.pi)
print('value of the planck constant',const.h)
print(2*const.nano)
v = 1
k_electron = 0.5*const.electron_mass*(v**2)
k_proton = 0.5*const.proton_mass*(v**2)
print("Kinetic Energy of prton", k_proton)
print("Kinetic Energy of electron", k_electron)
print("Ratio of K.E.",k_electron/k_proton)