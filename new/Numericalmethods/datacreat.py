from math import exp

with open("Numericalmethods\data.txt", "w") as f:

    for i in range(100):
        f.write(str(i) + "\t" + str(2 * exp(-0.5 * i)) + "\n")
