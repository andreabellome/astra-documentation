# `FGKepler_dt`

## DESCRIPTION
Kepler propagation of an orbit. This works also for hyperbolic paths.

## INPUT
- kep1 : 1x6 vector with initial keplerian elements (see car2kep.m)
- dt   : time of flight [s]
- mu   : gravitational parameter of the central body [km3/s2]

## OUTPUT
- rrf  : 1x3 vector of spacecraft position after the propagation [km]
- vvf  : 1x3 vector of spacecraft velocity after the propagation [km/s]
- kep2 : 1x6 vector of final keplerian elements after the propagation
(see car2kep.m)

## Function Signature
```matlab
[rrf, vvf, kep2] = FGKepler_dt(kep1, dt, mu)
```
