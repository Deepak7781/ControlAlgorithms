# Transfer Function for an armature controlled DC motor

In an armature controlled DC motor, the speed (angular velocity denoted as $\omega$) is regulated by varying the armature Voltage ($V_a$) while keeping the field flux constant.

The tranfer function we seek is $G(s)= \frac{\omega(s)}{V_a(s)}$, whers $s$is the Laplace variable. This relates the ouput speed in the s-domainto the input armature voltage.

Assumptions:

- The field winding is separately  excited or constant, so back EMF and torque constants are fixed.
- Load Torque $T_L = 0$ (unloaded for constant load; for small-signal analysis this is standard)
- All parameters are positive constants.
    - $R_a$ : Armature resistance
    - $L_a$ : Armature inductance
    - $K_b$ : Back-EMF constant
    - $K_t$ : Torque Constant
    - $J$   : Moment of Inertia of the rotor

### Step 1 - Electrical Circuit Equation

The armature circuit is modeled as a voltage source $V_a$ during a series RL circuit, opposed by the back EMF $E_b$. The back EMF is proportional to the speed : $E_b = K_b \omega$

$$V_a(t) = R_aI_a(t) + L_a \frac{dI_a}{dt} + E_b(t)$$

$$ V_a(t) = R_aI_a(t) + L_a \frac{dI_a}{dt} + K_b \omega(t) \tag{1} $$

where $I_a(t) is the armature current$

### Step 2 - Mechanical Dynamics Equation

The torque produced by the motor is T(t) = $K_tI_a(t)$. This torque accelerates the rotor against inertia and friction.

$$ T(t) = J\frac{d\omega(t)}{dt} + B\omega(t)$$
$$ K_tI_a(t) = J\frac{d\omega(t)}{dt} + B\omega(t) \tag{2}$$

### Step 3 - Laplace Transform of the equations

Electrical equation in s-domain

$$ 
    V_a(s) = R_aI_a(s) + L_asI_a(s) + K_b\omega(s) 
$$

solve for $I_a(s)$

$$
    I_a(s)(R_a + L_as) = V_a(s) - K_b\omega(s)
$$

$$  
    I_a(s) = \frac{V_a(s) - K_b\omega(s)}{R_a+L_as} 
$$

Mechanical Equation in s-domain

$$ K_tI_a(s) = Js\omega(s) + B\omega(s) $$

solve for $\omega(s)$

$$ K_tI_a(s) = (Js + B)\omega(s) $$

$$ \omega(s) = \frac{K_tI_a(s)}{Js+B} $$

substitue $I_a(s) $ in the above equation

$$ \omega(s) = \frac{K_t}{Js+B}\frac{V_a(s) - K_b\omega(s)}{R_a + L_as} $$

$$ \omega(s) (R_a + L_as) (Js+B) = [V_a(s) - K_b\omega(s)]K_t $$

$$ \omega(s) (R_a + L_as) (Js+B) = [K_tV_a(s) - K_bK_t\omega(s)] $$

$$ \omega(s) [(R_a + L_as) (Js+B) + K_bK_t] =K_tV_a(s)$$

$$ \frac{\omega(s)}{V_a(s)} = \frac{K_t}{(R_a + L_as) (Js+B) + K_bK_t} \tag{3} $$

$(3)$ is the Transfer Function for an armature controlled DC motor

In SI units $K_t = K_b = K$ as we use in the simulation

$$ \frac{\omega(s)}{V_a(s)} = \frac{K}{(R_a + L_as) (Js+B) + K^2} \tag{4} $$

$(4)$ is implemented in MATLAB and Simulink.