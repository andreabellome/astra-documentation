# `wrap_DynProgr_st2`

## DESCRIPTION:
This function performs dynamic programming for the second stage of the trajectory optimization.
It calculates and prunes potential trajectory legs, computes defects, and applies cost functions to determine
the optimal trajectory based on various constraints and input parameters.

## INPUT
- dsmOpts : Vector specifying the maximum allowed defect delta-v and other related parameters.

## INPUT:
LEGSnext : Matrix containing the possible trajectory legs for the current iteration, where each row represents
a leg with columns for departure and arrival planets, departure and arrival times, and the delta-v required.
VASnext  : Matrix containing the arrival velocities at the destination planets for each leg.
VINFn    : Vector containing the incoming velocities at the destination planets for each leg.
legs     : Matrix specifying the sequence of planets and associated indices for processing.
runOpts  : Matrix containing options for the Lambert solution, including the method and parameters.
indl     : Index of the current leg being processed.
tstep    : Time step for discretizing the trajectory.
TOF_LIM  : Limits for time of flight constraints.

## OUTPUT:
LEGSn  : Matrix containing the trajectory legs after applying dynamic programming, pruning, and cost functions.
VASn   : Matrix containing the arrival velocities for the filtered trajectory legs.
VINFn  : Vector containing the incoming velocities for the filtered trajectory legs.
nLP    : Number of possible legs considered in this stage.
nDEF   : Number of defects calculated for the current set of trajectory legs.

## Function Signature
```matlab
[LEGSn, VASn, VINFn, nLP, nDEF] = wrap_DynProgr_st2(LEGSnext, VASnext, legs, runOpts, indl, tstep, TOF_LIM, INPUT)
```
