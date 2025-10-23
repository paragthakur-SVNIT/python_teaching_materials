
def f(x):
    return x**3 - 5*x + 1

a = float(input("Enter first guess value: "))
b = float(input("Enter second guess value: "))
n = int(input("Enter number of iterations: "))

fa = f(a)
fb = f(b)

if fa * fb > 0:
    raise ValueError("Initial guesses should have different signs")

d = 0
for i in range(1, n+1):
    c = (a + b) / 2                   # Bisection
    # c = (a*fb - b*fa) / (fb - fa)   # Regula-Falsi / Secant
    
    fc = f(c)
    if abs(fc) < 0.0001:
        break
    
    if fc < 0:      # Bisection & Regula-Falsi
        a = c       # Bisection & Regula-Falsi  //b=c
        fa = fc     # Bisection & Regula-Falsi
        # a = b     # Secant
        #fa = fb    # Secant
    else:
        b = c
        fb = fc
        if abs(d - c) < 0.0001:
            break
        d = c
print("Iteration & Root Approximation:", i, c)
