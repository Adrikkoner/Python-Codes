import math


def func(x):
    return 1/(2*x -1)


print("Integration using Simpson's 1/3 rule")
a = float(input("Input the lower limit: "))
b = float(input("Input the higher limit: "))
intervals = int(input("Input the number of intervals: "))

h = float((b - a)) / float(intervals)
evenlist = []
oddlist = []
for i in range(1, intervals):
    if i % 2 == 0:
        evenlist.append(func(a + i * h))
    else:
        oddlist.append(func(a + i * h))

result = (func(a) + func(b) + 2 * sum(evenlist) + 4 * sum(oddlist)) * h / 3.0
print("The result of the integration is: ", result)
