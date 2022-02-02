import math


# for calculating u value
def ucal(u, p):
    temp = u
    for i in range(1, p):
        temp = temp * (u - i)
    return temp


n = 5

y = [[0 for i in range(n)] for j in range(n)]
x = [0.1, 0.2, 0.3, 0.4, 0.5]
y[0][0] = 1.10517
y[0][1] = 1.2140
y[0][2] = 1.34986
y[0][3] = 1.49182
y[0][4] = 1.64872
value = 0.411
u = (value - x[0]) / (x[1] - x[0])

# for calculating forward difference table
for i in range(1, n):
    for j in range(n - i):
        y[j][i] = y[j + 1][i - 1] - y[j][i - 1]

summ = y[0][0]
for i in range(1, n):
    summ += (ucal(u, i) * y[0][i]) / math.factorial(i)

print(f"the value at {value} is {summ}")
