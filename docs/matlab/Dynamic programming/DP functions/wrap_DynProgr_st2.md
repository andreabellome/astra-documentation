# `wrap_DynProgr_st2`

## INPUT
- dsmOpts : Vector specifying the maximum allowed defect delta-v and other related parameters.
OUTPUT:
LEGSn  : Matrix containing the trajectory legs after applying dynamic programming, pruning, and cost functions.
VASn   : Matrix containing the arrival velocities for the filtered trajectory legs.
VINFn  : Vector containing the incoming velocities for the filtered trajectory legs.
nLP    : Number of possible legs considered in this stage.
nDEF   : Number of defects calculated for the current set of trajectory legs.

## Function Signature
```matlab
[LEGSn, VASn, VINFn, nLP, nDEF] = wrap_DynProgr_st2(LEGSnext, VASnext, legs, runOpts, indl, tstep, TOF_LIM, INPUT)
```
