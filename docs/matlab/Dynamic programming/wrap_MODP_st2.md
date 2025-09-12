# `wrap_MODP_st2`

## DESCRIPTION
This function wraps the Multi-Objective Dynamic Programming (MODP) process for the
second stage of trajectory optimization. It evaluates possible trajectories for the
spacecraft, computes their feasibility, and prunes non-optimal paths using parallel
or sequential processing. The function ultimately selects and saves the best
trajectories based on a cost function.

## INPUT
- LEGSnext : Matrix containing the possible next legs (trajectories) of the spacecraft.
- VASnext  : Matrix of spacecraft velocities corresponding to LEGSnext.
- legs     : Matrix of initial trajectory legs (current mission plan).
- runOpts  : Options for running the dynamic programming algorithm.
- indl     : Index of the current leg being processed.
- tstep    : Time step used for generating the time of flight (TOF) array.
- TOF_LIM  : Limits on the time of flight for the leg.
- INPUT    : Struct containing additional input parameters, including DSM options
and the parallel processing flag.

## OUTPUT
- LEGSn    : Matrix containing the next legs after processing and optimization.
- VASn     : Matrix of spacecraft velocities corresponding to the selected next legs.
- VINFn    : Vector of spacecraft hyperbolic excess velocities for the selected next legs.
- nLP      : Number of launch points (nodes) generated for the leg.
- nDEF     : Number of defects found in the dynamic programming step.

## Function Signature
```matlab
[LEGSn, VASn, VINFn, nLP, nDEF] = wrap_MODP_st2(LEGSnext, VASnext, legs, runOpts, indl, tstep, TOF_LIM, INPUT)
```
