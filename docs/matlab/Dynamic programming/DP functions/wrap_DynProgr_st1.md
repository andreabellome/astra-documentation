# `wrap_DynProgr_st1`

## INPUT
OUTPUT:
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
