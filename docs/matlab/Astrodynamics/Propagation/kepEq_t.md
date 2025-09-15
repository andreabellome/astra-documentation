# `kepEq_t`

## DESCRIPTION:
It finds the time t corresponding to an angular position f. Elliptic
orbits (e < 1).

## INPUT:
-	f[1]    True anomaly [rad].
- a[1]    Semi-major axis [L].
- e[1]    Eccentricity.
- mu[1]   Planetary constant (mu = mass * G) [L^3/T^2].
- f0[1]   Fixed true anomaly [rad].
- t0[1]   Time corresponding to f0 [T].
> Optional: Default value = 0.

## OUTPUT:
-	t[1]    Time corresponding to f [T] between [-Inf, Inf].

## Function Signature
```matlab
[t] = kepEq_t(f, a, e, mu, f0, t0)
```
