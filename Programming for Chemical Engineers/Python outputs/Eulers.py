#algorithm for eulers method
import numpy as np
def f(x,y):
    return (x+y)
y=1
x=0
x=np.array[x]
y=np.array[y]
xn=1
h=0.1
print('Eulers method')
n=((xn-x)/h)
j=int(input('Enter approximation'))
for i in range (j):
    print('\n%g=%g\n',x[i],y[i])
    x[i+1]=x[i]+h
    y[i+1]=y[i]+h*f(x[i],y[i])