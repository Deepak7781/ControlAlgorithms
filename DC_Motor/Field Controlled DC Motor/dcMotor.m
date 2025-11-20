% Implementing a PID controller to a field controlled DC Motor
% The output is angular speed and input is field voltage



Ktf = 0.1; % Torque constant
Rf = 1.0;  % Field resistance
Lf = 0.5; % Field inductance
J = 0.01;  % Moment of inertia
B = 0.1;   % Damping coefficient (Viscous friction)


s = tf('s');

plant = Ktf/((J*s + B)*(Rf + s*Lf));

disp(plant);

plant_ss = ss(plant);

% disp(plant_ss)

%step(plant);

Kp = 130;
Ki = 200;
Kd = 10;

C = pid(Kp, Ki, Kd);

G = feedback(C*plant_ss, 1);

step(G)