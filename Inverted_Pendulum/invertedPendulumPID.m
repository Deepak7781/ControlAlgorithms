% Physical Parameters

m = 0.1; % Mass of pendulum in kg
M = 1.5; % Mass of the cart in kg
g = 9.81; % Acceleration due to gravity
l = 1; % Length of the pendulum in m

% Building the state space model
A = [0 1 0 0;
    0 0 -(m*g)/M 0;
    0 0 0 1;
    0 0 ((M+m)*g)/(M*l) 0];

B = [0; 1/M; 0; 1/(M*l)];

C = eye(4);

D = zeros(4,1);

G = ss(A, B, C, D);

G_tf = tf(G);