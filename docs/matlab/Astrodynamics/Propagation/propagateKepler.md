# `propagateKepler`

## DESCRIPTION
This function propagates in keplerian dynamics an initial state over a
grid of time of flights.

## INPUT
- rr1 : 1x3 vector with initial position [km]
- vv1 : 1x3 vector with initial velocity [km/s]
- tt  : 1xN vector with time of flights [s]
- mu  : gravitational constant of the central body [km3/s2]

## OUTPUT
- tt   : same as in input
- yy   : Nx6 matrix, where each row is the state, i.e., position and
velocity vectors evaluated at each tt(i)
- kkep : Nx6 matrix, where each row is a set of keplerian elements (see
car2kep.m) evaluated at each tt(i)

## Function Signature
```matlab
[tt, yy, kkep] = propagateKepler(rr1, vv1, tt, mu)
```
