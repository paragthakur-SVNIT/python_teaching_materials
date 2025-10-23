import numpy as np
A = np.array([[12, 3, -5], [1, 5, 3], [3, 7, 13]], dtype=float)
B = np.array([1, 28, 76], dtype=float)
n = len(B)
A = np.hstack((A, B.reshape(-1, 1)))
#print(A)
#for j in range(0,n-1):        #for gauss-elimination
#    for i in range(j+1,n):    #for gauss-elimination
for j in range(n):             #gauss-jordan
    A[j, :] = A[j, :] / A[j, j]    #gauss-jordan
    for i in range(n):             #gauss-jordan
        if i != j:
            m = A[i, j] / A[j, j]
            A[i, :] = A[i, :] - m * A[j, :]
print(A)
x = np.zeros(n)
for i in range(n-1, -1, -1):
    ax=np.sum(A[i, :-1] * x)
    x[i] = (A[i, -1] -ax ) / A[i, i]
    print(f"x({i+1}) = {x[i]}")




