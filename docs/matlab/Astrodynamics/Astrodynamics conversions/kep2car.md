# `kep2car`

## DESCRIPTION:
Converts from Keplerian orbital elements to Cartesian position and
velocity. All units to be consistent each other. Angles in radians.
Note: In the case of hyperbola, theta must be such that the point is on
the physical leg of the hyperbola (the leg around the attracting
mass).

## INPUT:
-	kep[6] :      Vector of keplerian elements: [a e i Om om theta], where
theta is the true anomaly. a in [L], angles in [rad].
In case of hyperbola (e>1), it must be: kep(1)<0.
- mu :          Planetary gravity constant [L^3/(M*T^2)].
- p :          Semi-latus rectum [L]. Only used for parabola case.

## OUTPUT:
- out[1,6]    State vector in cartesian coordinates (position [L],
velocity [L/T]).

## Function Signature
```matlab
[out] = kep2car(kep,mu,p)
```
