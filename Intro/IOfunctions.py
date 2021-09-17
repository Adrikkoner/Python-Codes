from math import *

# Console Input
a = input("Give me a number: ")
b = input("Give me another number: ")
c = float(a) * float(b)
print(c)

# File I/O

with open("myfile.txt", "w") as f:
    for i in range(100):
        f.write(str(i) + "\t" + str(factorial(i)) + "\n")
