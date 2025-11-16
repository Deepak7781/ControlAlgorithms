J = 0.01;
B = 0.1;
K = 0.01;
R = 1;
L = 0.5;

s = tf('s');
P_motor = K/((J*s+B)*(L*s+R)+K^2);

% disp(P_motor);

% step(P_motor);
% ramp(P_motor);

% kp = 100;
% controller = pid(kp);
% 
% clsys = feedback(controller*P_motor, 1);
% 
% t = 1:0.05:5;
% step(clsys, t);
% grid
% % Plot the step response of the closed-loop system
% title('Step Response of Closed-Loop System');
% xlabel('Time (s)');
% ylabel('Response');


kp = 100;
ki = 200;
kd = 10;

C = (kp*s + ki + kd*s^2)/s;

%controller = pid(kp, ki, kd);

clsys = feedback(C*P_motor, 1);
t = 0:0.01:4;
step(clsys, t);
grid
% Plot the step response of the closed-loop system
title('Step Response of Closed-Loop System');
xlabel('Time (s)');
ylabel('Response');


