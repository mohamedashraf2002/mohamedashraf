
import numpy as np
import sys
n = 3

a = np.zeros((n, n + 1))
x = np.zeros(n)
# take  matrix coefficients
print('Enter Augmented Matrix Coefficients:')
for i in range(n):
    for j in range(n + 1):
        a[i][j] = float(input('a[' + str(i) + '][' + str(j) + ']='))
# Applying Gauss Jordan Elimination
for i in range(n):
    if a[i][i] == 0.0:
        sys.exit('Can’t Divide by zero  (error!)')
    for j in range(n):
        if i != j:
            ratio = a[j][i] / a[i][i]

            for k in range(n + 1):
                a[j][k] = a[j][k] - ratio * a[i][k]
print(a)
#  Solution
for i in range(n):
    x[i] = a[i][n] / a[i][i]
# Displaying solution
print('\nRequired solution is: ')
for i in range(n):
    print('X%d = %0.2f' % (i, x[i]), end='\t')
