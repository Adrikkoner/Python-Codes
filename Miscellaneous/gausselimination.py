# Importing NumPy Library
import numpy as np
import sys
n = 4
# Making numpy array of n x n+1 size and initializing 
# to zero for storing augmented matrix
a = np.array([[4.0,-4,3,2,5],[5,6,7,8,3],[-9,7,-5,3,-30],[1,1,1,1,2]])

# Making numpy array of n size and initializing 
# to zero for storing solution vector
x = np.zeros(n)

print(a)
# Applying Gauss Elimination
for i in range(n):
    if a[i][i] == 0.0:
        sys.exit('Divide by zero detected!')
        
    for j in range(i+1, n):
        ratio = a[j][i]/a[i][i]
        
        for k in range(n+1):
            a[j][k] = a[j][k] - ratio * a[i][k]

# Back Substitution
x[n-1] = a[n-1][n]/a[n-1][n-1]

for i in range(n-2,-1,-1):
    x[i] = a[i][n]
    
    for j in range(i+1,n):
        x[i] = x[i] - a[i][j]*x[j]
    
    x[i] = x[i]/a[i][i]

# Displaying solution
print('\nRequired solution is: ')
for i in range(n):
    print('X%d = %0.2f' %(i,x[i]), end = '\t')