def f(x):
    return x**3 - 3*x - 5

def f_deri(x, h=0.001):
    return (f(x + h) - f(x - h)) / (2 * h)
a = float(input("Enter first guess value: "))
b = float(input("Enter second guess value: "))
n = int(input("Enter number of iterations: "))
fa = f(a)
fb = f(b)
if fa * fb > 0:
    raise ValueError("Initial guesses should be different")
x = a if (fa + fb) > 0 else b
d = 0  
for i in range(1, n+1):
    x = x - f(x) / f_deri(x)    
    if abs(d - x) < 0.0001:       
        break
    d = x
print("Iteration & Root Approximation:", i, x)
