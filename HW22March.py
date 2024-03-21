import numpy as np
import matplotlib.pyplot as plt

##############################
# Parameters
##############################
length_x = 3.2
length_y = 3.2
dt = 0.001

grid_x = 32
grid_y = 32
n_t = 128

gamma = 1


##############################
# Initialization
##############################
x = np.linspace(0, length_x, grid_x)
y = np.linspace(0, length_y, grid_y)
X, Y = np.meshgrid(x, y)

u = np.zeros((n_t,grid_x,grid_y))
u[0,:,:] = np.sin(4 * np.pi * X/length_x) + np.cos(4 * np.pi * Y/length_y)


##############################
# Computation
##############################
dx = length_x/(grid_x-1)
dy = length_y/(grid_y-1)

for i in range(n_t - 1):
    for j in range(1, grid_x - 1):
        for l in range(1, grid_y - 1):
            dux = (u[i, j + 1, l] - 2 * u[i, j, l] + u[i, j - 1, l]) / dx**2
            duy = (u[i, j, l + 1] - 2 * u[i, j, l] + u[i, j, l - 1]) / dy**2
            u[i + 1, j, l] = u[i, j, l] + gamma * dt * (dux + duy)
# u[-1,0,:] = u[0,0,:]
# u[-1,-1,:] = u[0,-1,:]
# u[-1,:,0] = u[0,:,0]
# u[-1,:,-1] = u[0,:,-1]

plt.figure()
plt.imshow(u[-1, 1:-1, 1:-2], extent=[0, length_x, 0, length_y], origin='lower', cmap='coolwarm')
plt.colorbar(label='Temperature')
plt.xlabel('x')
plt.ylabel('y')
plt.title('2D Heat Equation')
plt.savefig('2D_Heat')

