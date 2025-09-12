# `wrap_DynProgr_st1`

## DESCRIPTION:
This function performs the first stage of dynamic programming for interplanetary trajectory optimization.
It computes the possible legs, associated velocities, and incoming velocities for the next stage, considering
the initial conditions and constraints. The function supports parallel processing to speed up calculations.

## INPUT:
T0      : Initial time (epoch) for the departure from the first planet.
legs    : Matrix representing the sequence of planetary encounters, where each row corresponds to a leg.
runOpts : Vector containing options for the Lambert solver, such as the method for solving the Lambert problem.
tstep   : Time step (in days) used for generating possible times of flight.
TOF_LIM : Vector containing the minimum and maximum time of flight limits for the legs.

## OUTPUT:
LEGSnext : Matrix containing the possible trajectory legs for the next stage, including the departure and arrival planets,
departure and arrival times, and the delta-v required.
VASnext  : Matrix containing the arrival velocities at the destination planets for each leg.
VINFnext : Vector containing the incoming velocities at the destination planets for each leg.
tocVec   : Scalar representing the elapsed time for the function execution.
nLP      : Scalar representing the number of possible legs for the next stage.

## Function Signature
```matlab
[LEGSnext, VASnext, VINFnext, tocVec, nLP] = wrap_DynProgr_st1(T0, legs, runOpts, tstep, TOF_LIM, INPUT)
```
