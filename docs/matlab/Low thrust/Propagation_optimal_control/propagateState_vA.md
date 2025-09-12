# `propagateState_vA`

## DESCRIPTION:
This function is used to compute the difference between target final
state and final state resulting from the propagation. The states are
given in Mean Equinoctial Elements (MEE).

## INPUT:
- lambda0      : 7x1 vector with initial conditions for co-states
- propFunction : MATLAB anonymous function of time and states (e.g., see
propagateFopt_MEXIFY.m or propagateEopt_MEXIFY.m)
- pm           : structure with parameters for the propagation

## OUTPUT:
F : 6x1 vector with difference between target final state and final state
resulting from the propagation.

## Function Signature
```matlab
[F] = propagateState_vA(lambda0, propFunction, pm)
```
