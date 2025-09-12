# `maxRev_LP`

## DESCRIPTION
This function computes the maximum number of revolutions allowed for a
Lambert arc based on the given time of flight and positions. It provides
an estimate of how many full revolutions can fit within the provided
transfer time, assuming the minimum semi-major axis for the two-body
orbit connecting the input positions.

## INPUT
- tof_days   : time of flight for the transfer arc [days]
- rr1        : initial position vector [km]
- rr2        : final position vector [km]
- muCentral  : gravitational parameter of the central body [km^3/s^2]

## OUTPUT
- NumRevMax : maximum number of full revolutions feasible within the
given time of flight [-]

## Function Signature
```matlab
[NumRevMax] = maxRev_LP(tof_days, rr1, rr2, muCentral)
```
