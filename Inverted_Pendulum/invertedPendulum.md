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
    R_x = \ddot{x} + ml\ddot{\theta}cos\theta - ml\dot{\theta}^2sin\theta
$$


