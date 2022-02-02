import numpy as np
from matplotlib import pyplot as plt
from scipy.special import legendre

# x = np.linspace(0, 1, 100)
# for i in range(1,6):
#    plt.plot(x, legendre(i)(x))
# plt.show()

from scipy.special import jv

x = np.linspace(0, 10, 100)
for i in range(6):
    plt.plot(x, jv(i, x))
plt.show()
