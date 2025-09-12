# `eci2synodic_eph`

## DESCRIPTION
This function converts state vectors from the ECI (Earth-Centered Inertial)
reference frame to the Synodic reference frame, given the state vector of
a secondary body (e.g., Moon), and the gravitational parameters of both
primary and secondary bodies.

## INPUT
- Xeci  : State vector in the ECI reference frame [position; velocity].
- svbody: State vector of the secondary body at a particular epoch [position; velocity].
- mu1   : Gravitational parameter of the primary body (e.g., Earth).
- mu2   : Gravitational parameter of the secondary body (e.g., Moon).

## OUTPUT
- Xsyn  : State vector in the Synodic reference frame [position; velocity].
- L_ref : Distance from the primary body to the secondary body.
- V_ref : Velocity of the secondary body relative to the primary body.

## Function Signature
```matlab
[Xsyn, L_ref, V_ref] = eci2synodic_eph(Xeci, svbody, mu1, mu2)
```
