#Algorithm for 2D Heat Equation
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

Lx, Ly = 0.1, 0.1; nx, ny = 21, 21
dx, dy = Lx/(nx-1), Ly/(ny-1)
alpha = 0.01; dt = 0.0001; nt = 1000

Fox = alpha * dt / dx**2; Foy = alpha * dt / dy**2

if Fox + Foy > 0.5:
    raise ValueError("Unstable scheme! Reduce dt or refine grid.")

x = np.linspace(0, Lx, nx)
y = np.linspace(0, Ly, ny)
X, Y = np.meshgrid(x, y, indexing='ij') 

T = np.exp(-5*((X-0.5)**2 + (Y-0.5)**2))

T[0,:] = 0; T[-1,:] = 0
T[:,0] = 0; T[:,-1] = 0

zmax_init = np.max(T)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(X, Y, T, cmap='viridis')
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("Temperature")
ax.set_zlim(0, zmax_init)
ax.set_title("2D Heat Conduction")

mappable = plt.cm.ScalarMappable(cmap='inferno')
mappable.set_array(T)
cbar = fig.colorbar(mappable, ax=ax, shrink=0.5, aspect=10)
cbar.set_label("Temperature")

def update(frame):
    global T
    Told = T.copy()
    T[1:-1,1:-1] = Told[1:-1,1:-1] + \
                    Fox*(Told[2:,1:-1] - 2*Told[1:-1,1:-1] + Told[0:-2,1:-1]) + \
                    Foy*(Told[1:-1,2:] - 2*Told[1:-1,1:-1] + Told[1:-1,0:-2])
    
    ax.clear()
    surf = ax.plot_surface(X, Y, T, cmap='viridis')
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("Temperature")
    ax.set_zlim(0, zmax_init)
    ax.set_title(f"2D Heat Conduction at step {frame*20}")
    return surf

ani = FuncAnimation(fig, update, frames=nt//20, interval=50, blit=False)
plt.show()
