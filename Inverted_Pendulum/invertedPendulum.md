# Nonlinear Mathematical Modeling of an Inverted Pendulum Using Newton's Laws

## Introduction

The inverted pendulum is one of the most important benchmark problems in dynamics and control systems. It consists of a pendulum mounted on a horizontally moable cart. The objective is to apply a horizontal force to the cart in such a way that the pendulum remains balanced in its upight unstable equilibrium position

## System Description

The system has a cart of mass $M$ that slides horizontally, with a pendulum of mass $m$ and length $l$ pinned at the cart's center. The control input is the horizontal force F applied to the cart. The state variables are cart position $x$, cart velocity $\dot{x}$, pendulum angle $\theta$ (from vertical) and angular velocity $\dot{\theta}$  

![Inverted Pendulum System](diagram.png)

## Coordinate System and Sign Convention

Let, 
- $x$ = horizontal displacement of the cart
- $\theta$ = angular displacement of the pendulum measured from the vertical

where positive $x$ direction is towards the right and positive $\theta$ direction is taken clockwise from the upward vertical position.

The pendulum is assumed to be a rigid rod of length $l$ with point mass $m$ concentrated at its end. The cart is free to move only in the horizontal direction.

## Position of the Pendulum mass

The coordinates of the pendulum mass can be wriiten using simple trigonometry.

Horizontal position of the pendulum mass:

$$
    x_p = x + lsin\theta
$$

Vertical position of the pendulum mass:

$$
    y_p = lcos\theta
$$

where, 
- $x_p$ = horizontal position of pendulum mass
- $y_p$ = vertical position of the epndulum mass

## Velocity of the pendulum mass

Differentiating the position equations with respect to time,

$$
    \dot{x}_p = \dot{x} + l\dot{\theta}cos\theta
$$

$$
    \dot{y}_p = -l\dot{\theta}sin\theta
$$

Again Differentiating,

$$
    \ddot{x}_p = \ddot{x} + l\ddot{\theta}cos\theta - l\dot{\theta}^2sin\theta
$$

$$
    \ddot{y}_p = -l\ddot{\theta}sin\theta - l\dot{\theta}^2cos\theta
$$

These equations represent the horizontal and vertical accelerations of the pendulum mass.

## Free body diagram of the pendulum mass

Considering the forces acting on the pendulum mass,

The forces acting on the pendulum mass are:
- Horizontal reaction force at pivot $R_x$
- Vertical reaction force at pivot $R_y$
- Weight of pendulum $mg$

Appyling Newton's second law in horizontal direction,

$$
    \Sigma F_x = m \ddot{x}_p 
$$

Therefeore, 

$$
    R_x = m \ddot{x}_p
$$

sub $\ddot{x}_p$

$$
    R_x = m(\ddot{x} + l\ddot{\theta}cos\theta - l\dot{\theta}^2sin\theta)
$$

Hence, 

$$
    R_x = m\ddot{x} + ml\ddot{\theta}cos\theta - ml\dot{\theta}^2sin\theta
$$

## Free Body Diagram of the Cart

Now consider tge cart of mass M

The horizontal forces acting on the cart are:
- Applied control force $F$
- Reaction force from pendulum $R_x$

Applying Newton's second law

$$
    \Sigma F_x = m \ddot{x}
$$

Therefore,

$$
    F - R_x = M \ddot{x}
$$

sub $R_x$

$$
F - (m\ddot{x} + ml\ddot{\theta}cos\theta - ml\dot{\theta}^2sin\theta) = M \ddot{x}
$$

$$
F = M \ddot{x} + (m\ddot{x} + ml\ddot{\theta}cos\theta - ml\dot{\theta}^2sin\theta)
$$

$$
F = (M+m)\ddot{x} + ml\ddot{\theta}cos\theta - ml\dot{\theta}^2sin\theta
$$

Thus the first nonlinear equation of motion becomes,

$$
    \boxed{(M+m)\ddot{x} + ml\ddot{\theta}cos\theta - ml\dot{\theta}^2sin\theta=F}
$$

## Tangential Motion of the Pendulum

To derive the angular equation of motion, Newtons second law is applied in the tangential direction of the pendulum motion.

Before directly applying Newton's law, it is important to understand how the tangential direction is obtained.

### Radial and Tangential Directions

The pendulum moves along a circular path of radius $l$. 

For any body moving in a circular path, the motion can be resolved into two mutually perpendicular directions:
- Radial direction
- Tangential direction

The radial direction is along the pendulum rod toward the pivot.

The tangential direction is perpendicular to the rod and along the instantaneous direction of motion of the pendulum mass. 

Since the angular displacement of the pendulum is represented by $\theta$, the tangential direction is the direction in which $\theta$ increases.

### Tangential Unit Vector

The pendulum rod makes an angle $\theta$ with the vertical.

The position vector of the pendulum mass from the pivot is,

$$
    \vec{r} = \begin{bmatrix}
                lsin\theta \\
                lcos\theta
                \end{bmatrix}
$$

Dividing by $l$, the radial unit vector becomes

$$
    \hat{e}_r = \begin{bmatrix}
                \sin\theta \\
                \cos\theta
                \end{bmatrix}
$$

The tangential direction must always be perpendicular to the radial direction.

Rotating the radial vector by $90 \degree$ clockwise gives the tangential unit vector.

$$
    \hat{e}_t = \begin{bmatrix}
                \cos\theta \\
                -\sin\theta
                \end{bmatrix}
$$

This vector points along the direction of increasing $\theta$

### Acceleration of the Pendulum Mass

From the previous derivation,

$$
    \ddot{x}_p = \ddot{x} + l\ddot{\theta}\cos\theta - l\dot{\theta}^2\sin\theta
$$

$$
    \ddot{y}_p = -l\ddot{\theta}\sin\theta - l\dot{\theta}^2\cos\theta
$$

Therefore, the acceleration vector of the pendulum mass is,

$$
    \vec{a}_p = \begin{bmatrix}
                \ddot{x}_p \\
                \ddot{y}_p
                \end{bmatrix}
$$

Substituting the acceleration components,

$$
    \vec{a}_p = \begin{bmatrix}
                \ddot{x} + l\ddot{\theta}\cos\theta - l\dot{\theta}^2\sin\theta \\
                -l\ddot{\theta}\sin\theta - l\dot{\theta}^2\cos\theta
                \end{bmatrix}
$$

### Tangential Acceleration

The tangential acceleration is the component of total acceleration along the tangential direction.

This is obtained using the dot product between the acceletration vector and the tangential unit vector.

Thus, 

$$
    a_t = \vec{a}_p \cdot \hat{e}_t
$$

$$
    a_t = \begin{bmatrix}
                \ddot{x} + l\ddot{\theta}\cos\theta - l\dot{\theta}^2\sin\theta \\
                -l\ddot{\theta}\sin\theta - l\dot{\theta}^2\cos\theta
                \end{bmatrix}

                \cdot

                \begin{bmatrix}
                \cos\theta \\
                -\sin\theta
                \end{bmatrix}
$$

$$
    a_t = (\ddot{x} + l\ddot{\theta}\cos\theta - l\dot{\theta}^2\sin\theta)\cos\theta - (-l\ddot{\theta}\sin\theta - l\dot{\theta}^2\cos\theta)\sin\theta
$$

$$
    a_t = \ddot{x}\cos\theta + l\ddot{\theta}\cos^2\theta - l\dot{\theta}^2\sin\theta\cos\theta + l\ddot{\theta}\sin^2\theta + l\dot{\theta}^2\sin\theta\cos\theta
$$

$$
    a_t = \ddot{x}\cos\theta + l\ddot{\theta}(\sin^2\theta + \cos^2\theta)
$$

$$
    a_t = \ddot{x}\cos\theta+l\ddot{\theta}
$$

### Tangential Component of Gravity

The weight vector acting on the pendulum mass is,

$$
    \vec{W} = \begin{bmatrix}
                0 \\
                -mg
                \end{bmatrix}
$$

The tangential component of gravity is obtained by projecting the weight vector onto the tangential direction.

Thus,

$$
    W_t = \vec{W}\cdot\hat{e}_t
$$

$$
    W_t = \begin{bmatrix}
                0 \\
                -mg
                \end{bmatrix} \cdot
                \begin{bmatrix}
                \cos\theta \\
                -\sin\theta
                \end{bmatrix}
$$

$$
    W_t = mg\sin\theta
$$

This is the component of gravity responsible for rotating the pendulum.

### Applying Newton's Second Law in Tangential Direction

$$
    \Sigma F_t = m a_t
$$

Substituting the tangential force and tangential aceleration.

$$
    mg\sin\theta = m(\ddot{x}\cos\theta+l\ddot{\theta})
$$

$$
 g\sin\theta = (\ddot{x}\cos\theta+l\ddot{\theta})
$$

$$
 \boxed{l\ddot{\theta} + \ddot{x}\cos\theta - g\sin\theta = 0}
$$

This is the nonlinear angular equation of motion of the inverted pendulum system.

## Final Nonlinear Equations of Motion 

Hence, the complete nonlinear mathematical model of the inverted pendulum system is given by

$$
    \boxed{(M+m)\ddot{x} + ml\ddot{\theta}cos\theta - ml\dot{\theta}^2sin\theta=F}
$$

$$
 \boxed{l\ddot{\theta} + \ddot{x}\cos\theta - g\sin\theta = 0}
$$

These equations completely describe the nonlinear coupled dynamics of the inverted pendulum system.

## Linearization of Nonlinear Eqautions of Motion

### Need for Linearization

The non-linear equations describe the exact dynamics of the system over thr entire operating range.

However, the Linear Quadratic Regulator (LQR) is derived for systems represented in the linear form

$$
    \dot{X} = Ax + Bu
$$

Hence, the nonlinear equations must forst be linearized.

The objective of linearization is to approximate the nonlinear system by a linear system near a chosen operating point.

For the inverted pendulum, the operating point is the upright equilibrium configuration.

### Upright Equilibrium Configuration

The upright equilibrium corresponds to:
- $x=0$
- $\dot{x}=0$
- $\theta = 0$
- $\dot{\theta} = 0$
- $F = 0$

At this condition: 
- the cart is stationary
- the pendulum is perfectly upright
- no control force is applied

The controller is designed to maintain the system near this equilibrium position.

### Small Angle Approximation

Since the pendulum operates near the upright equilibrium position, the angular displacement remains small.

For small values of $\theta$

$$
    \sin\theta \approx \theta
$$

$$
    \cos\theta \approx 1
$$

Also, $\sin^2\theta \approx 0$

Higher-order nonlinear terms are neglected. In particular, $\dot{\theta}^2\sin\theta$ is neglected because it is a higher nonlinear term.

### Linearization of Cart Equation

Starting with the nonlinear cart equation,

$$
    (M+m)\ddot{x} + ml\ddot{\theta}\cos\theta - ml\dot{\theta}^2\sin\theta = F
$$

Applying small-angle approximations, $\cos\theta \approx 1$ and neglecting $\dot{\theta}^2\sin\theta$

gives,

$$
    (M+m)\ddot{x} + ml\ddot{\theta} = F
$$

Thus, the linearized cart equations becomes,

$$
    \boxed{(M+m)\ddot{x} + ml\ddot{\theta} = F}
$$

### Linearization of Pendulum Equation

The nonlinear pendulum equation is,

$$
    l\ddot{\theta} + \ddot{x}\cos\theta - g\sin\theta = 0
$$

Applying the approximations,

$$
    \cos\theta \approx 1
$$

$$
    \sin\theta \approx \theta
$$

gives,

$$
    l\ddot{\theta} + \ddot{x}\ - g\theta = 0
$$

Thus, the linearized pendulum equation becomes,

$$
    \boxed{l\ddot{\theta} + \ddot{x}\ - g\theta = 0}
$$

### Linearized Equations of Motion

The complete set of linearization equations is therefore:

Cart Equation,

$$
    \boxed{(M+m)\ddot{x} + ml\ddot{\theta} = F}
$$

Pendulum Equation,

$$
    \boxed{l\ddot{\theta} + \ddot{x}\ - g\theta = 0}
$$

The equations describe the system dynamics near the upright equilibrium position.

## State-Space Model

### Solving for $\ddot{x}$ and $\ddot{\theta}$

From Pendulum equation, 

$$
    \ddot{x} = g\theta - l\ddot{\theta}
$$

Substituting into Cart equation

$$
    (M + m)(g\theta - l\ddot{\theta}) + ml\ddot{\theta} = F
$$

$$
    (M + m)g\theta - (M + m)l\ddot{\theta} + ml\ddot{\theta} = F
$$

$$
    (M+m)g\theta - Ml\dot{\theta} - ml\ddot{\theta} + ml\ddot{\theta} = F
$$

$$
    (M+m)\ddot{\theta} - Ml\ddot{\theta} = F
$$

$$
    Ml\ddot{\theta} = (M+m)g\theta - F
$$

$$
    \boxed{\ddot{\theta} = \frac{(M+m)g\theta}{Ml} - \frac{1}{Ml}F}
$$

Substituting $\ddot{\theta}$ back to the pendulum equation

$$
    \ddot{x} = g\theta - l\left(\frac{(M+m)g\theta}{Ml} - \frac{1}{Ml}F\right)
$$

$$
    \ddot{x} = g\theta - \frac{(M+m)g\theta}{M} + \frac{1}{M}F
$$

$$
    \ddot{x} = g\theta - \frac{Mg\theta}{M} - \frac{mg\theta}{M} +\frac{1}{M}F
$$

$$
    \ddot{x} = \frac{-mg\theta}{M} + \frac{1}{M}F
$$

Thus,

$$
    \boxed{\ddot{x} = \frac{-mg\theta}{M} + \frac{1}{M}F}
$$

### Formation of State variables

The system currently consists of second-order differential equations.

State-space representaion requires first-order equations.

Hence the following state variables are defined:

$$
x_1 = x
$$

$$
x_2 = \dot{x}
$$

$$
x_3 = \theta
$$

$$
x_4 = \dot{\theta}
$$

Thus, the state vector becomes

$$
X = \begin{bmatrix}
        x_1 \\ x_2 \\ x_3 \\ x_4
    \end{bmatrix}
    =
    \begin{bmatrix}
        x \\ \dot{x} \\ \theta \\ \dot{\theta}
    \end{bmatrix}
$$

### Formation of First-Order Stae Equations