from scipy import optimize
def f(x):
    return (x**3 - 1)  # only one real root at x = 1
def fprime(x):
    return 3*x**2

sol = optimize.root_scalar(f, bracket=[0, 3], method='brentq')
print(sol.root, sol.iterations)

sol = optimize.root_scalar(f, x0=0.2, fprime=fprime, method='newton')
print(sol.root, sol.iterations)

def fun_rosenbrock(x):
    return np.array([10 * (x[1] - x[0]**2), (1 - x[0])])

