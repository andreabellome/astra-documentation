# `postProcessLT_SEP`

## DESCRIPTION
This function processes the results of a low-thrust trajectory optimization
by converting scaled states back to physical units, extracting the thrust
profile, and assembling all relevant trajectory data into a single matrix.

## INPUT
- time         : Vector of time points (scaled units).
- states       : Matrix of state vectors (scaled units), where each row
corresponds to a time step and contains [position, velocity, mass].
- propFunction : Function handle for the propulsion model, which returns
the thrust profile in the RTN frame.
- pm           : Parameter structure containing constants and scaling factors,
including:
- MU        : Mass unit (kg).
- LU        : Length unit (km).
- TU        : Time unit (s).
- muScl     : Scaled gravitational parameter.
- TmaxScl   : Scaled maximum thrust.
- IspScl    : Scaled specific impulse.
- g0Scl     : Scaled gravitational acceleration.
- rho       : Density parameter for the propulsion model.

## OUTPUT
- transfer : Matrix containing the processed trajectory data with the
following columns:
[time (days), position (km), velocity (km/s), mass (kg),
thrust magnitude (N), thrust vector (N)].

## Function Signature
```matlab
[transfer] = postProcessLT_SEP( time, states, propFunction, pm )
```
