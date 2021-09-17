from scipy import constants as const
import numpy as np
from matplotlib import pyplot as plt

initial_wavelength = 400*const.nano
final_wavelength = 700*const.nano

wavelengths = np.linspace(initial_wavelength,final_wavelength,2000)
energyarray=[]
for wavelength in wavelengths:
    energy= (const.h*const.c)/(wavelength*const.electron_volt)
    energyarray.append(energy)
energyarray = np.array(energyarray)
fig, ax = plt.subplots()  # Create a figure and an axes.
ax.plot(wavelengths, energyarray, label="Energy")  # Plot some data on the axes.
ax.set_xlabel("lambda")  # Add an x-label to the axes.
ax.set_ylabel("E")  # Add a y-label to the axes.
ax.set_title("Energy vs wavelength")  # Add a title to the axes.
ax.legend()  # Add a legend.
plt.show()