# `kepEq_t`

## DESCRIPTION:
It finds the time t corresponding to an angular position f. Elliptic
orbits (e < 1).

## INPUT:
f[1]    True anomaly [rad].
a[1]    Semi-major axis [L].
e[1]    Eccentricity.
mu[1]   Planetary constant (mu = mass * G) [L^3/T^2].
f0[1]   Fixed true anomaly [rad].
t0[1]   Time corresponding to f0 [T].
> Optional: Default value = 0.

## OUTPUT:
t[1]    Time corresponding to f [T] between [-Inf, Inf].
CALLED FUNCTIONS:
(none)
FUTURE DEVELOPMENT:
Extension to parabolic and hyperbolic orbits.
ORIGINAL VERSION:
Camilla Colombo, 20/02/2006, MATLAB, tl.m
AUTHOR:
Camilla Colombo, Nicolas Croisard, 20/11/2007, MATLAB, kepEq_t.m
PREVIOUS VERSION:
Camilla Colombo, 20/11/2007, MATLAB, tl_inf.m
- Time corresponding to f [T] given in the range [-Inf, Inf].
Camilla Colombo, Nicolas Croisard, 20/11/2007, MATLAB, tl3.m
- Header and function name in accordance with guidlines.
CHANGELOG:
02/12/2008, Matteo Ceriotti: Optional argument t0.
02/12/2008, REVISION: Matteo Ceriotti
30/12/2009, Camilla Colombo: Header and function name in accordance
with guidlines.

## Function Signature
```matlab
[t] = kepEq_t(f, a, e, mu, f0, t0)
```
