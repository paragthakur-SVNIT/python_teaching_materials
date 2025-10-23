
#gauss elimination method and gauss jordan method
import numpy as np
import matplotlib.pyplot as plt
A=np.array([[12, 3, -5], [1, 5, 3], [3, 7, 13]],dtype=float)
b=np.array([[1],[28],[76]])
n=len(b)
a=np.hstack((A, b))
for j in range(n-1):        # Gauss Elimination
#for j in range(n):         # Gauss Jordan 
    #a[j,:]=a[j,:]/a[j,j]   # Gauss Jordan
    #for i in range(n):     # Gauss Jordan
    for i in range (j+1,n): # Gauss Elimination
        if i!=j:            
            m=a[i,j]/a[j,j]
            a[i,:]=a[i,:]-(m*a[j,:])
x=np.zeros(n)
print(a)
for i in range(n-1,-1,-1):
    ax=np.sum(a[i,i+1:n]*x[i+1:n])
    x[i] = (a[i, -1] - ax) / a[i, i]
    print("\nSolution (Gauss Elimination):", x[i])

plt.figure(figsize=(5,4))
plt.bar(range(1, n+1), x)
plt.title("Solution of Linear System (Gauss Elimination)")
plt.xlabel("Variable Index")
plt.ylabel("Value")
plt.show()