import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Parameters
L = 1.0
nx = 20
dx = L / (nx - 1)
alpha = 0.01
dt = 0.0005
nt = 200
Fo = alpha * dt / (dx**2)

x = np.linspace(0, L, nx)

# Initial condition
T = np.exp(-200*(x-0.5)**2)
T[0] = 0.0
T[-1] = 0.0

# Store history
Tsol = np.zeros((nt+1, nx))
Tsol[0, :] = T

for t in range(1, nt+1):
    Told = T.copy()
    for i in range(1, nx-1):
        T[i] = Told[i] + Fo * (Told[i+1] - 2*Told[i] + Told[i-1])
    T[0], T[-1] = 0.0, 0.0
    Tsol[t, :] = T

# --- Animation ---
fig, ax = plt.subplots()
line, = ax.plot(x, Tsol[0], '-o')
ax.set_ylim(0, 1)
ax.set_xlabel("x (rod length)")
ax.set_ylabel("Temperature")

def update(frame):
    line.set_ydata(Tsol[frame])
    ax.set_title(f"1D Heat Conduction – Time step {frame}")
    return line,

ani = FuncAnimation(fig, update, frames=range(0, nt+1, 2), interval=100)

# Save as video (requires ffmpeg installed)
ani.save("heat_conduction.mp4", writer="ffmpeg")

plt.show()
