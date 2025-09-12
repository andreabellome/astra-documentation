# `findDV`

## DESCRIPTION
This function computes DV defects.

## INPUT
- vvrel_A : 1x3 vector with incoming relative velocity [km/s]
- vvrel_D : 1x3 vector with outgoing relative velocity [km/s]
- muPL    : gravitational parameter of the flyby body [km3/s2]
- rpmin   : minimum flyby periapsis [km]

## OUTPUT
- dv      : DV defect manoeuvre [km/s]
- alpha   : deflection required for the flyby [rad]
- alpha_A : max. deflection for the minimum periapsis flyby [rad]

## Function Signature
```matlab
[dv, alpha, alpha_A] = findDV(vvrel_A, vvrel_D, muPL, rpmin)
```
