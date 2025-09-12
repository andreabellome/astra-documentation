# `propagateKepler_tof`

## DESCRIPTION
This function propagates in keplerian dynamics an initial state for a
specified time of flight.

## INPUT
- rr1     : 1x3 vector with initial position [km]
- vv1     : 1x3 vector with initial velocity [km/s]
- tof     : time of flight [sec]
- mu      : gravitational constant of the central body [km3/s2]
- npoints : number of points for the propagation (default: 500)

## OUTPUT
- tt   : same as in input
- yy   : Nx6 matrix, where each row is the state, i.e., position and
velocity vectors evaluated at each tt(i)
- kkep : Nx6 matrix, where each row is a set of keplerian elements (see
car2kep.m) evaluated at each tt(i)

## Function Signature
```matlab
[tt,yy] = propagateKepler_tof(rr1, vv1, tof, mu, npoints)
```
