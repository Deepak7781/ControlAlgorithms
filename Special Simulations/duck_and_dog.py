# Duck and Dog Simulation

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

T = 50
dt = 0.001
Tsim = np.arange(0, T, dt)

R = 1
phi = 0
theta = np.radians(0)

x_duck = []
y_duck = []

x_dog = []
y_dog = []

R_hist = []

k = 1.5 # Speed ratio (Dog speed/Duck speed)
for i in range(len(Tsim)):

    x_duck.append(np.cos(theta))
    y_duck.append(np.sin(theta))

    x_dog.append(x_duck[i] - (R*np.cos(theta + phi)))
    y_dog.append(y_duck[i] - (R*np.sin(theta + phi)))

    R_hist.append(R)

    dRdtheta = np.sin(phi) - k
    dphidtheta = (np.cos(phi)/R) - 1

    # Euler Integration
    R = R + dRdtheta*dt
    phi = phi + dphidtheta*dt
    theta = theta + dt

    if R <= 0.001:
        break


fig, ax = plt.subplots()
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.plot(np.cos(np.linspace(0,2*np.pi, 1000)), np.sin(np.linspace(0,2*np.pi, 1000)), 'k--', linewidth=1, label="Pond Boundary")
ax.grid(True)

duck, = ax.plot([], [], 'mo', label = "Duck")
dog, = ax.plot([], [], color = 'brown', marker = 'o', label = "Dog")
dogTrail, = ax.plot([], [], color = 'saddlebrown', linewidth = 1, label = "Dog Trail")
message = ax.text(0,0,"",fontsize=15,   ha='center')
ax.axis('equal')
ax.legend(loc = 'best')

Trail_Length = 500
def update(frame):
    duck.set_data([x_duck[frame]], [y_duck[frame]])
    dog.set_data([x_dog[frame]], [y_dog[frame]])
    start = max(0, frame - Trail_Length)
    dogTrail.set_data(x_dog[start:frame+1], y_dog[start:frame+1])
    return duck, dog, dogTrail, message

ani = FuncAnimation(fig, update, frames = len(Tsim), interval = dt, blit = True)

plt.show()