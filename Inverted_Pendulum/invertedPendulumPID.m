% Physical Parameters

m = 0.1; % Mass of pendulum in kg
M = 1.5; % Mass of the cart in kg
g = 9.81; % Acceleration due to gravity
l = 1; % Length of the pendulum in m

% Building the state space model
s = tf('s');
G = 1/((M+m)*g - M*l*s^2);

Kp = 10;
Ki = 0.5;
Kd = 5;

C = pid(Kp, Ki, Kd);

cl_sys = feedback(G, C);

step(cl_sys)
