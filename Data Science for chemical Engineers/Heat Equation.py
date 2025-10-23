#Algorithm for 1D Heat Equation 
import numpy as np
import matplotlib.pyplot as plt

L = 1.0; nx = 20; dx = L / (nx - 1); alpha = 0.01
dt = 0.0005; nt = 200  

Fo = alpha * dt / (dx**2)

if Fo > 0.5:
    print("Warning: Scheme unstable. Reduce dt or increase nx.")

x = np.linspace(0, L, nx)

T = np.sin(np.pi * x / L)
T[0] = 0.0; T[-1] = 0.0

plt.ion() 
fig, ax = plt.subplots()

for t in range(1, nt + 1):
    Told = T.copy()
    for i in range(1, nx - 1):
        T[i] = Told[i] + Fo * (Told[i+1] - 2*Told[i] + Told[i-1])

    if t % 20 == 0:
        ax.clear()
        ax.plot(x, T, '-o')
        ax.set_title(f"1D Heat Conduction (Explicit FD)\nTime step {t}")
        ax.set_xlabel("x (rod length)")
        ax.set_ylabel("Temperature")
        ax.set_ylim(0, 1)   
        plt.pause(0.1)      
plt.ioff()
plt.show()
