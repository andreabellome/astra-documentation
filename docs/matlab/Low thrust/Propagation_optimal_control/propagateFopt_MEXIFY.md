# `propagateFopt_MEXIFY`

## DESCRIPTION:
This function propagates the spacecraft dynamics in two-body problem and
applies the fuel-optimal (time-fixed) control.

## INPUT:
- t       : time [LU]
- xvalues : 7x1 vector with MEE and mass (adimensional variables)
- pp      : 4x1 vector with:
- pp(1) : mu [LU3/TU2] -- gravitational parameter of the
central body
- pp(2) : TmaxScl [adim] -- max. thrust
- pp(3) : IspScl [TU] -- specific impulse
- pp(4) : g0Scl [LU/TU2] -- Earth's gravitational
acceleration at sea level

## OUTPUT:
- dx     : accelerations of the state vector (i.e., xvalues)
- thrust : 3x1 thrust vector (adim.)
- m      : mass (adim.)

## Function Signature
```matlab
[dx, thrust, m] = propagateFopt_MEXIFY( t, xvalues, pp )
```
