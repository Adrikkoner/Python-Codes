from scipy.integrate import quad

def func(x):
    return 1/(2*x -1)
lower_limit = 1
upper_limit = 3
result = quad(func,lower_limit,upper_limit)
print("The result of the integration is: ", result[0])
