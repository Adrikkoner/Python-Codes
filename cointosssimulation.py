import random

def cointoss40():
    head = 0
    tail = 0
    for i in range(39):
        r = random.random()
        if r >= 0.5:
            head += 1
        else:
            tail += 1
    return(head, tail)

thirtyhead = 0
N = 1000000
for i in range(N):
    head, tail = cointoss40()
    if head == 30:
        thirtyhead += 1
    #print(head, tail)
print("Simulation is running with steps", N)
print("Probability of 30 head =", 1.0 * thirtyhead/N)