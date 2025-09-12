# `M2theta`

## DESCRIPTION
Conversion from mean anomaly to true anomaly for keplerian orbits. Also
works for hyperbolic paths. Newton method is used.

## INPUT
- M : mean anomaly
- e : eccentricity

## OUTPUT
- theta :true anomaly [rad]

## Function Signature
```matlab
[theta] = M2theta(M, e)
```
