import control
import numpy as np
import matplotlib.pyplot as plt

# Physical Parameters
m = 0.1 # mass of pendulum in kg
M = 1.5 # mass of cart in kg
g = 9.81
l = 1 # length of pendulum in m

# Building State-space representation
A = np.array([[0,1,0,0], [0, 0, -(m*g)/M, 0], [0,0,0,1], [0, 0, ((M+m)*g)/(M*l), 0]])
B = np.array([[0], [1/M], [0], [-1/(M*l)]])
C = np.array([[1, 0, 0, 0], [0, 1, 0, 0],[0, 0, 1, 0], [0, 0, 0, 1]])
D = np.array([[0], [0], [0], [0]])

G = control.ss(A, B, C, D)
print("State-space representation of the inverted pendulum system:")
print(G)

# LQR Controller Design
Q = np.diag([1, 1, 100, 1])
R = np.array([[0.01]])

K, S, E = control.lqr(G, Q, R)
print("LQR Gain Matrix K:")
print(K)

# Build Closed-loop system
G_cls = control.ss(A - B @ K, B, C, D)
print("Closed-loop system with LQR controller:")
print(G_cls)

# Simulate the response to an initial condition
t = np.linspace(0, 10, 1000)
x0 = np.array([0, 0, 0.1, 0]) # initial state: small angle deviation
t, y = control.forced_response(G_cls, T=t, U=0*t, X0=x0)

plt.plot(t, y.T)
plt.title("Response of Inverted Pendulum with LQR Control")
plt.xlabel("Time (s)")
plt.ylabel("States")
plt.legend(["Cart Position", "Cart Velocity", "Pendulum Angle", "Pendulum Angular Velocity"])
plt.grid()
plt.show()