# Indrotuction to PID Controllers

A **PID controller**(Propoertional-Integral-Derivative controller) is the most widely used feedback control strategy in engineering systems. It is employed in applications rangng from DC motor speed control, robotics, aircraft flight control, automotive engines, industrial process control, to power systems. The reason for its popularity is its simplicity, robustness, and ability to provide stable and accurate control without requiring a complete mathematical model of the system.

At its core, a PID controller continuously compares the reference (desired value) with the actual output of the system and generates a control signal that attempts to minimize the difference between them. This difference is known as the error signal, defined as

$$
    e(t) = r(t) - y(t)
$$

where $r(t)$ is the refernece input and $y(t)$ is the system output

The PID computes its control action using three separate components:

- **Proportional (P)** - produces control action proportional to the current error
- **Integral (I)** - produces control action based on accumulated past errors
- **Derivative (D)** -produces control action based on the predicted future behavior of the error

These three components are combined to form the complete control law:

$$
    u(t) = K_pe(t) + K_I \int_0^te(\tau)d\tau + K_D \frac{de(t)}{dt}
$$

Each term plays a unique role in shaping the system's response.

- The **Proportional** term reduces the overall error by reacting immediately to the difference between commanded and actual output.
- The **Integral** term eliminates steady-state error by accumulating error over time and providing long-term adjustment.
- The **Derivative** term predicts system behavior by sensing how rapidly the error is changing and adds damping to reduce overshoot and oscillations.

Because these three actions complement each other, a PID controller can achieve fast response, high accuracy, and stab;e operation even when system dynaics are nonlinear or uncertain. It does not  require complex optimization or advanced modeliing, which makes ir extremely practical for real-world systems sucha as DC motors, where loads and operating conditions frequently change.

## The Three PID Components

### 1. Proptional Control (P-term)

$$
    u_p(t) = K_pe(t)
$$

**Meaning of the formula**

* The control output is directly proportional to instantaneous error.
* If error doubles, control action also doubles

How P actually works

* P simply multiplies that error by a gain $K_p$

**What happens inside the loop**

1. Suppose the motor speed is below reference, it gives a positive error
2. P multiplies the error by $K_p$ which results in higher motor voltage
3. The increased voltage results in more current which produces more torque and the speed increases
4. As speed gets closer to reference error decreases so the P output also decreases
5. When speed reaches reference exactly, error becomes zero and the P output becomes zero.

**Why P creates a steady-state error**

To maintain a non-zero output voltage (needed to overcome motor driction and back-EMF) P needs non-zero error

Example:

The motor may need 2 V to run at 1000 rpm. But when the motor is at the reference speed, the error is zero.

$$
    u_p = K_p\cdot0 = 0
$$

So the motor cannot keep running, eventually the speed drops and the error reappears, so the P provides the needed 2 V.

This leads to an equilibrium point where:

$$
    u_p = K_pe_{ss}
$$

Error at steady state is

$$
    e_{ss} = u_{needed}/K_p
$$

Hence, 

* Larger $K_p$ &rarr; smaller error 
* But too large $K_p$ &rarr; oscillations

### Integral Control (I-term)

$$
    u_I = K_I \int_0^t e(\tau) d\tau
$$

**Meaning of the formula**

* I adds up (accumulates) error over time
* Even a tiny persistent error accumulates into a large correction

**How I actually works**

* Suppose motor is running at 950 rpm when the target is 1000 rpm.
* Error $\approx$ 50
* Even if this error is small, it stays for many seconds.
* Integraton keeps summing the 50 rpm error
* The longer the error persists, the larger will be the integral output.
* Eventually, the integral term grows large enough to supply the extract additional voltage needed to eliminate the error.

**Why integral removes steady-state error**

* P can only react to instantaneous error
* But I reacts to past acccumulated error

Even if error is tiny:

$$
    u_I(t) = K_I (50t)
$$

This keeps increasing until the motor reaches refernce speed; when error becomes zero the integral stops growing.

**Final Effect**

I automatically produces the constant voltage needed to overcome back-EMF, friction, load torque, etc.

**Why Integral causes overshhot**

Integral has "memory". If the motor takes time to reach setpoint, the integral keeps growing. Even if the motor reaaches reference, integral may still be large. Thus the controller continues pushing the motor, causing overshhot. This phenomenon is called **Integral windup**.

### Derivative Control (D-term)

$$
    u_D(t) = K_D \frac{de(t)}{dt}
$$

**Meaning of the formula**

* D reacts to the rate of change of error
* It sees the trend of your system, whether the error is rising or failing, how fast.

**How D behaves**

Derivative looks at the slope the error curve

Example:

If motor speed is increasing quicking and approaching the setpoint, error is decreasing rapidly

$$
    \frac{de(t)}{dt}
$$

This means:

* Error is heading toward zero too fast, so possible overshoot.
* D produces a negative output to oppose rapid change

**Why D reduces Overshoot**

If the motor is speeding up too quickly:

* P pushes the motor hard because eroor is large
* I pushes the motor because the accumulated error is large.
* D notices that error is shrinking very fast, so it produces a strong negative output.
* This shows down the control effort, which prevents the overshoot.

**Why D improves stability**

Derivative adds "damping" to the control system, similar to a shock absorber.

Mathematically,it counteracts high frequency changes:

* If error oscillates, derivative becomes large &rarr; D pushes back &rarr; damping oscillations

**Why D is sensitive to noise**

Error signal directly differentiates noise:

$$
    \frac{d(noise)}{dt} \approx \text{huge spikes}
$$

Hence real controllers use filtered derivative instead of pure derivative.
