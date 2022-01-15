import math


def func(x):
    return x ** (-1.5)


print("Integration using Trapezoidal rule")
a = float(input("Input the lower limit: "))
b = float(input("Input the higher limit: "))
intervals = int(input("Input the number of intervals: "))

h = float((b - a)) / float(intervals)
valuelist = []
for i in range(1, intervals):

    valuelist.append(func(a + i * h))

result = (func(a) + func(b) + 2 * sum(valuelist)) * h / 2.0
print("The result of the integration is: ", result)
