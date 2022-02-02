import random
import numpy as np
from matplotlib import pyplot as plt

def cointoss40():
    head = 0
    tail = 0
    for i in range(39):
        result = random.random()
        if result >= 0.5:
            head += 1
        else:
            tail += 1
    return (head, tail)


N = 1000
tailcount=[]
for j in range(N):
    headres, tailres = cointoss40()
    tailcount.append(tailres)
print("Simulation is running with steps", N)
tailcount = np.array(tailcount)
index = np.arange(1,N+1)
plt.plot(index, tailcount)
plt.show()
