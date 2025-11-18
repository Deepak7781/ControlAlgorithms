# Transfer function of a field controlled DC Motor

The derivation of the transfer function for a field - controlled DC motor relates the angular displacement or speed of the motor shaft (output) to the field voltage (input) assuming the armature current is kept constant.

The system is governed by two main sets of sets of equations: the electrical system (field  circuit) and the mechanical system (rotor and load)

### Step 1 : Electrical System (Field Circuit) Equations

The field circuit consists of a field winding with resistance $R_f$ and inductance $L_f$ when a control voltage $V_f(t)$ is applied, the voltage equation by Kirchhoff's voltage law is

$$
    V_f(t) = R_fi_f(t) + L_f \frac{di_f(t)}{dt}-->(1)
$$

where 

- $V_f(t)$ is the applied field voltage (input)
- $i_f(t)$ is the field current

### Step 2 : Mechanical System Equations

In a DC motor, the developed torque $T_m(t)$ is proportional to the product of the air gap flux $\phi$ and the armature current $i_a(t)$

- For a field-controlled motor, the armature current $i_a(t)$ is held constant.
- The flux $\phi$ is proportional to the field current $i_f(t)$, so  $\phi \propto i_f(t)$

Therefore, the motor torque is proportional to the field current

$$
    T_m(t) \propto i_f(t)
$$

$$
    T_m(t) = K_{t_f} i_f(t)-->(2)
$$

where $K_{t_f}$ is the motor torque constant for field control

The torque also drives the mechanical load, which includes the rotor's inertia $J$ and viscous friction $B$

The mechanical equation of motion is

$$
    T_m(t) = J\frac{d^2\theta(t)}{dt^2} + B\frac{d\theta(t)}{dt} -->(3)
$$

### Step 3 : Laplace Transform of the Equations

Assuming zero initial conditions, we take the Lapalce transform of the governing equations $(1),(2), (3)$

Laplace transform of $(1)$

$$
    V_f(s) = R_fI_f(s) + sL_fI_f(s)
$$

$$
    V_f(s) = (R_f + sL_f)I_f(s)-->(4)
$$

Laplace transform of $(2)$

$$
    T_m(s) = K_{t_f}I_f(s)-->(5)
$$

Laplace transform of $(3)$

$$
    T_m(s) = Js^2\Theta(s) + Bs\Theta(s)
$$

$$
    T_m(s) = (Js^2 + Bs)\Theta(s)-->(6)
$$

### Transfer Function

From $(6)$

$$
    \Theta(s) = \frac{T_m(s)}{Js^2 + Bs} --> (7)
$$

$\frac{(7)}{(4)} \implies \frac{\Theta(s)}{V_f(s)}$

$$
    \frac{\Theta(s)}{V_f(s)} = \frac{T_m(s)}{Js^2 + Bs}\times\frac{1}{(R_f + sL_f)I_f(s)}
$$

Substituting $T_m(s)$ from $(5)$

$$
    \frac{\Theta(s)}{V_f(s)} = \frac{K_{t_f}I_f(s)}{Js^2 + Bs}\times\frac{1}{(R_f + sL_f)I_f(s)}
$$

$$
    \frac{\Theta(s)}{V_f(s)} = \frac{K_{t_f}}{(Js^2 + Bs)(R_f + sL_f)}
$$

$$
    \frac{\Theta(s)}{V_f(s)} = \frac{K_{t_f}}{s(Js + B)R_f(1 + \frac{sL_f}{R_f})}
$$

Let 

- $K_m = \frac{K_{t_f}}{BR_f}$ - (Motor Gain constant)

- $\tau_f = \frac{L_f}{R_f}$ - (Field Time Constant)

- $\tau_m = \frac{J}{B}$ - (Mechanical Time constant)

The final transfer function for Angular Displacement $\frac{\Theta(s)}{V_f(s)}$ is

$$
    \frac{\Theta(s)}{V_f(s)} = \frac{K_m}{s^2\tau_f\tau_m + s(\tau_f+\tau_m)+s}
$$

A more simplified and common form using the constants:

$$
    \frac{\Theta(s)}{V_f(s)} = \frac{K_{t_f}/R_fB}{s(1 + \frac{sL_f}{R_f})(1 + \frac{sJ}{B})}
$$

If the output is the Angular speed , $\Omega(s)=s\Theta(s)$

$$
    \frac{\Omega(s)}{V_f(s)} = \frac{K_{t_f}}{(Js+B)(R_f+sL_f)}
$$