# `postProcessPathASTRA_lowThrust`

## DESCRIPTION
This function processes the output of a low-thrust trajectory optimization
problem to generate a structured output. It calculates velocity adjustments
(DSM), ephemerides, and departure/arrival states, while considering constraints
such as flyby conditions and central body parameters.

## INPUT
- path      : matrix describing the trajectory, including object IDs and epochs
- vdep      : scalar, maximum departure velocity (default is 0 if not provided)
- varr      : scalar, maximum arrival velocity (default is 0 if not provided)
- idcentral : scalar, central body identifier (default is 1 for Sun)

## OUTPUT
- struc : structure containing detailed information about the trajectory,
including departure and arrival states, velocity adjustments,
and ephemerides for each transfer leg.

## Function Signature
```matlab
[struc] = postProcessPathASTRA_lowThrust(path, vdep, varr, idcentral, customEphemerides)
```
