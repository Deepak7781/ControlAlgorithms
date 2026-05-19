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

% Choose Q and R
Q = [1 0 0 0;
     0 1 0 0;
     0 0 1 0;
     0 0 0 1];

R = 0.01;

% Building the Controller
[K, S, E] = lqr(A, B, Q, R);

% Form the Closed Loop Model
cl_sys = feedback(G, K);

% Response for Initial Disturbance
x0 = [0; 0; 0.3; 0]; % 0.1 rad ≈ 5.7° perturbation
[y, tout] = initial(cl_sys, x0);
y_theta_deg = y(:,3)*(180/pi);

% Plotting Upright Equilibrium
plot(tout, y_theta_deg);
xlabel("Time (s)");
ylabel("Theta (degree)");
grid on;

% Animation
x     = y(:,1);   % cart position
theta = y(:,3);   % pendulum angle from upright, rad

% Animation
figure;
for i = 1:5:length(tout)

    clf;
    hold on;
    grid on;
    axis equal;

    % Cart dimensions
    cart_width  = 0.4;
    cart_height = 0.2;

    % Cart position
    cart_x = x(i);
    cart_y = 0;

    % Pendulum bob position
    pend_x = cart_x + l*sin(theta(i));
    pend_y = cart_y + l*cos(theta(i));

    % Draw ground
    plot([-3 3], [0 0], 'k', 'LineWidth', 2);

    % Draw cart
    rectangle('Position', ...
        [cart_x - cart_width/2, cart_y - cart_height/2, cart_width, cart_height], ...
        'FaceColor', [0.6 0.6 0.6]);

    % Draw pendulum rod
    plot([cart_x pend_x], [cart_y pend_y], 'r', 'LineWidth', 3);

    % Draw pendulum bob
    plot(pend_x, pend_y, 'bo', 'MarkerSize', 12, 'MarkerFaceColor', 'b');

    % Draw pivot
    plot(cart_x, cart_y, 'ko', 'MarkerSize', 6, 'MarkerFaceColor', 'k');

    xlabel('Cart Position x (m)');
    ylabel('Height (m)');
    title(sprintf('Inverted Pendulum Animation, t = %.2f s', tout(i)));

    xlim([-2 2]);
    ylim([-0.5 1.5]);

    drawnow;
end