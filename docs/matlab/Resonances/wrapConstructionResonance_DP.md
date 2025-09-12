# `wrapConstructionResonance_DP`

## DESCRIPTION
This function attempts to construct resonant orbits for a spacecraft trajectory
by checking if resonances can be achieved and then generating the corresponding
resonant orbits. It operates in both parallel and sequential modes.

## INPUT
- LEGSnext : Matrix containing the legs of the spacecraft's trajectory, where each row
corresponds to a different leg.
- VASnext  : Matrix containing the spacecraft's velocities corresponding to each leg.
- VINFnext : Matrix containing the hyperbolic excess velocities for each leg.
- legs     : Matrix containing the initial legs of the trajectory.
- res      : Array containing the desired resonance ratio [numerator, denominator].
- indl     : Index identifying the specific leg to analyze in the 'legs' matrix.
- tolINCL  : Tolerance for inclination matching during resonance construction.
- parallel : Boolean flag to indicate whether to run the resonance checks in parallel.

## OUTPUT
- LEGSn  : Matrix of legs after constructing resonant orbits.
- VASn   : Matrix of velocities after constructing resonant orbits.
- VINFn  : Matrix of hyperbolic excess velocities after constructing resonant orbits.

## Function Signature
```matlab
[LEGSn, VASn, VINFn] = wrapConstructionResonance_DP(LEGSnext, VASnext, VINFnext, legs, res, indl, tolINCL, parallel, idcentral, customEphemerides)
```
