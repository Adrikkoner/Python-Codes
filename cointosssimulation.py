import random


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


THIRTY_HEAD = 0
N = 1000000
for j in range(N):
    headres, tailres = cointoss40()
    if headres == 30:
        THIRTY_HEAD += 1
    # print(head, tail)
print("Simulation is running with steps", N)
print("Probability of 30 head =", 1.0 * THIRTY_HEAD / N)
