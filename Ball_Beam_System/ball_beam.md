# Derivation of the Transfer Function for the Ball and Beam System

## Introduction


The ball and beam system is a classic control engineering benchmark used to demonstrate concepts like instability, linearization, and feedback control. It consists of a beam pivoted at one end, with a ball that rolls along its length. The goal is to control the ball's position $r(t)$ by adjusting the beam's angle $\alpha(t)$, typically actuated by a servo motor via a lever mechanism.
The system is inherently nonlinear due to the gravitational force component $\sin \alpha$. The transfer function is obtained by linearizing the dynamics around the equilibrium point (horizontal beam, $\alpha = 0$, ball stationary).
This document derives the open-loop transfer function $G(s) = \frac{R(s)}{\Theta(s)}$, where $R(s)$ is the Laplace transform of the ball position $r(t)$, and $\Theta(s)$ is the Laplace transform of the servo angle $\theta(t)$ (related to $\alpha(t)$ by a gear ratio).


### System Parameters

$m$: Mass of the ball (kg)
$R$: Radius of the ball (m)
$g$: Acceleration due to gravity (m/s², ≈ 9.81)
$J$: Moment of inertia of the ball about its center (for a solid sphere, $J = \frac{2}{5} m R^2$)
$L$: Length of the beam (m)
$d$: Distance from the pivot to the actuator attachment point (often $d = L/2$)

### Assumptions:

The ball rolls without slipping.
Friction is negligible except for rolling.
Small angles for linearization ($\sin \alpha \approx \alpha$, $\cos \alpha \approx 1$).
The beam is massless or its inertia is included in the servo model (not considered here for the core dynamics).

### Nonlinear Equations of Motion
### Ball Dynamics
The ball experiences a gravitational force component along the inclined beam:
$$ F_g = -m g \sin \alpha $$
(directed towards the pivot for positive $\alpha$).
For rolling without slipping, the ball's translational acceleration $\ddot{r}$ and rotational acceleration $\dot{\omega} = \ddot{r}/R$ are coupled.

 The total kinetic energy includes translation and rotation, leading to an effective inertia.
From Newton's second law for translation:
$$ m \ddot{r} = F_g - f $$
where $f$ is the friction force providing torque for rotation.

For rotation:
$$ J \dot{\omega} = f R \implies f = \frac{J \ddot{r}}{R^2} $$

Substitute:
$$ m \ddot{r} = -m g \sin \alpha - \frac{J \ddot{r}}{R^2} $$

$$ \ddot{r} \left( m + \frac{J}{R^2} \right) = -m g \sin \alpha $$
$$ \ddot{r} = -\frac{m g \sin \alpha}{m + \frac{J}{R^2}} $$

For a solid sphere:

$$ J = \frac{2}{5} m R^2 \implies \frac{J}{R^2} = \frac{2}{5} m \implies m + \frac{J}{R^2} = \frac{7}{5} m $$

$$ \ddot{r} = -\frac{5 g \sin \alpha}{7} $$

### Beam Angle Relation

The beam angle $\alpha(t)$ is controlled via a servo motor with shaft angle $\theta(t)$. Assuming a simple lever mechanism:

$$ \alpha = \frac{d}{L} \theta $$
(For $d = L/2$, $\alpha = \theta / 2$.)

Thus, the nonlinear equation is:

$$ \ddot{r} = -\frac{5 g}{7} \sin \left( \frac{d}{L} \theta \right) $$

Linearization
For small angles ($\theta \approx 0$, $\alpha \approx 0$):

$$ \sin \alpha \approx \alpha = \frac{d}{L} \theta $$

$$ \ddot{r} \approx -\frac{5 g}{7} \cdot \frac{d}{L} \theta \ddot{r} + \frac{5 g d}{7 L} \theta = 0 $$

In the Laplace domain (zero initial conditions):

$$ s^2 R(s) = -\frac{5 g d}{7 L} \Theta(s) $$

$$ \frac{R(s)}{\Theta(s)} = -\frac{5 g d}{7 L s^2} $$

## Transfer Function
The linearized open-loop transfer function is:

$$ G(s) = \frac{R(s)}{\Theta(s)} = -\frac{K}{s^2} $$

where the gain $K = \frac{5 g d}{7 L}$.

### Typical Values

$g = 9.81$ m/s²
$d = L/2$, $L = 0.425$ m (common lab setup, e.g., Quanser)
$ K \approx \frac{5 \times 9.81 \times (0.425/2)}{7 \times 0.425} \approx 1.5 \, \frac{\mathrm{m}}{\mathrm{rad}} $

### Notes on Variations

No Rolling (Slipping Ball): If the ball slides without rotating ($J = 0$), $K = \frac{g d}{L}$.
Full System (Including Servo): Cascade with the DC servo motor transfer function (from armature voltage $V_a(s)$ to $\theta(s)$):
$ G_{\text{full}}(s) = G_{\text{servo}}(s) \cdot G(s) $
where $G_{\text{servo}}(s) \approx \frac{K_m}{s (\tau_m s + 1)}$ (second-order approximation).
Stability: The double pole at $s = 0$ indicates marginal stability; any disturbance causes unbounded growth, necessitating feedback control (e.g., PID).

Verification and Simulation
This derivation aligns with standard references (e.g., Franklin's Feedback Control of Dynamic Systems).
For simulation in MATLAB/Simulink or Python (using control library):
matlab