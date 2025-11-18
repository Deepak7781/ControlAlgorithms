import control as ct
import matplotlib.pyplot as plt

K = 0.1
J = 0.01
B = 0.1
R = 1
L = 0.5

dcMotor_tf = ct.tf([K], [J*L, J*R + B*L, B*R + K**2])

Kp, Ki, Kd = 100, 200, 10 
C = ct.tf([Kd, Kp, Ki], [1, 0])  # Note: s^2 coeff for num

# Closed-loop
T = ct.feedback(C * dcMotor_tf, 1)
t, y = ct.step_response(T)

plt.plot(t, y); plt.xlabel('Time'); plt.ylabel('Speed'); plt.show()