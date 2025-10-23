# Finite Difference Method
import numpy as np
import matplotlib.pyplot as plt

x0 = 0; xn = 9; y0 = 0; yn = 0
h = 1

x = np.arange(x0, xn + h, h) 
n = int((xn - x0) / h)

A = np.zeros((n-1, n-1))
B = np.zeros((n-1, 1))

for i in range(n-1):
    xi = x[i+1] 

    p = 0
    q = -2
    r = 8 * xi * (9 - xi)

    a = (1/h**2) - (p/(2*h))
    b = -(2/h**2) + q
    c = (1/h**2) + (p/(2*h))
    d =r

    if i > 0:
        A[i, i-1] = a
    A[i, i] = b
    if i < n-2:
        A[i, i+1] = c
    B[i] = d
Y_internal = np.linalg.solve(A, B)

Y = np.vstack(([y0], Y_internal, [yn]))

print('x values:')
print(x)
print('y values:')
print(Y.flatten())

plt.plot(x, Y, 'o-', label="Finite Difference Solution")
plt.xlabel('x')
plt.ylabel('y')
plt.title('Finite Difference Method Solution')
plt.grid(True)
plt.legend()
plt.show()
