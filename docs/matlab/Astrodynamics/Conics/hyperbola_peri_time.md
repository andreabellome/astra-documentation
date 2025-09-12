# `hyperbola_peri_time`

## DESCRIPTION:
Time since periapsis (and time to periapsis) passage on a hyperbola given
a true anomaly.

## INPUT
- a  : semi-major axis (km), negative for hyperbola
- e  : eccentricity (>1)
- mu : gravitational parameter (km^3/s^2)
- f  : true anomaly (rad)

## OUTPUT
- t_since_peri : time since periapsis (s). Positive if after periapsis.
- t_to_peri    : time to periapsis (s). Positive if periapsis is in the future.
- H            : hyperbolic anomaly (signed)

## Function Signature
```matlab
[t_since_peri, t_to_peri, H] = hyperbola_peri_time(a, e, mu, f)
```
