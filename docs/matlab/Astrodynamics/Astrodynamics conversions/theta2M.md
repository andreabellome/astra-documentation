# `theta2M`

## DESCRIPTION
Conversion from true anomaly to mean anomaly for keplerian orbits. Also
works for hyperbolic paths.

## INPUT
- theta : true anomaly [rad]
- e     : eccentricity

## OUTPUT
- M : mean anomaly

## Function Signature
```matlab
[M] = theta2M(theta, e)
```
