#Comparison of Results of Eulers method, Modified Eulers Method & RK-4 Method
import numpy as np
import matplotlib.pyplot as plt

k = 0.05

def f(t, Ca):
    return -k * Ca**2

t0 = 0; Ca0 = 1; tf = 100; h = 5
n = int((tf - t0) / h)

t_euler = np.zeros(n+1)
Ca_euler = np.zeros(n+1)
t_euler[0], Ca_euler[0] = t0, Ca0

for i in range(n):
    t_euler[i+1] = t_euler[i] + h
    Ca_euler[i+1] = Ca_euler[i] + h * f(t_euler[i], Ca_euler[i])

t_mod_euler = np.zeros(n+1)
Ca_mod_euler = np.zeros(n+1)
t_mod_euler[0], Ca_mod_euler[0] = t0, Ca0

for i in range(n):
    t_mod_euler[i+1] = t_mod_euler[i] + h
    Ca_pred = Ca_mod_euler[i] + h * f(t_mod_euler[i], Ca_mod_euler[i])
    Ca_mod_euler[i+1] = Ca_mod_euler[i] + (h/2) * (f(t_mod_euler[i], Ca_mod_euler[i]) + f(t_mod_euler[i+1], Ca_pred))

t_rk4 = np.zeros(n+1)
Ca_rk4 = np.zeros(n+1)
t_rk4[0], Ca_rk4[0] = t0, Ca0

for i in range(n):
    k1 = h * f(t_rk4[i], Ca_rk4[i])
    k2 = h * f(t_rk4[i] + h/2, Ca_rk4[i] + k1/2)
    k3 = h * f(t_rk4[i] + h/2, Ca_rk4[i] + k2/2)
    k4 = h * f(t_rk4[i] + h, Ca_rk4[i] + k3)
    
    Ca_rk4[i+1] = Ca_rk4[i] + (k1 + 2*k2 + 2*k3 + k4) / 6
    t_rk4[i+1] = t_rk4[i] + h

plt.figure(figsize=(8,6))
plt.plot(t_euler, Ca_euler, '-ob', label="Euler")
plt.plot(t_mod_euler, Ca_mod_euler, '-sg', label="Modified Euler")
plt.plot(t_rk4, Ca_rk4, '-^r', label="RK-4")

plt.xlabel("Time (s)")
plt.ylabel("Concentration C_A (mol/L)")
plt.title("Comparison of Methods for 2nd-order Batch Reactor")
plt.legend()
plt.grid(True)
plt.show()
