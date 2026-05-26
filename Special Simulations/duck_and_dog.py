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

k = 1.2 # Speed ratio (Dog speed/Duck speed)
for i in range(len(Tsim)):

    x_duck.append(np.cos(theta))
    y_duck.append(np.sin(theta))

    x_dog.append(x_duck[i] - (R*np.cos(theta + phi)))
    y_dog.append(y_duck[i] - (R*np.sin(theta + phi)))

    dRdtheta = np.sin(phi) - k
    dphidtheta = (np.cos(phi)/R) - 1

    # Euler Integration
    R = R + dRdtheta*dt
    phi = phi + dphidtheta*dt
    theta = theta + dt

    if R <= 0.001:
        break


