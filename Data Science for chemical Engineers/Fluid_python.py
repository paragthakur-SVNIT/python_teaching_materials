import numpy as np

# Parameters
D = 0.05     # pipe diameter (m)
L = 10       # length (m)
u = 1.0      # velocity (m/s)
rho = 1000   # density (kg/m3)
mu = 0.001   # viscosity (Pa.s)
eps = 0.0001 # roughness (m)

# Reynolds number
Re = rho * u * D / mu

# Colebrook residual function
def f(fric):
    return 1/np.sqrt(fric) + 2*np.log10((eps/D)/3.7 + 2.51/(Re*np.sqrt(fric)))

# Numerical derivative
def f_deri(fric, h=1e-6):
    return (f(fric + h) - f(fric - h)) / (2*h)

# User input (one initial guess)
x = float(input("Enter initial guess value for friction factor (e.g. 0.02): "))
n = int(input("Enter maximum number of iterations: "))

d = 0  

# Newton-Raphson iterations
for i in range(1, n+1):
    x = x - f(x)/f_deri(x)
    if abs(d - x) < 1e-6:   # convergence tolerance
        break
    d = x

# Pressure drop
dP = x * (L/D) * (rho*u**2/2)

print("Iteration:", i)
print("Friction factor:", x)
print("Pressure drop (Pa):", dP)
