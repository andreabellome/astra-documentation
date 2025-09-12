# `path2Vinfs`

## DESCRIPTION
This function computes the v-infinity vectors at each leg of a trajectory
path. It calculates both the departure and arrival v-infinity vectors and
their magnitudes based on the input path data.

## INPUT
- path : Matrix where each row represents a state in the trajectory with
columns for position (x, y, z), velocity (vx, vy, vz),
planetary ID, time, and v-infinity.
- idcentral : ID of the central body. See constants.m

## OUTPUT
- VINFS : Matrix containing the departure and arrival v-infinity vectors
and their magnitudes for each leg of the trajectory.
- vvd   : Matrix of v-infinity vectors at the departure of each leg.
- vva   : Matrix of v-infinity vectors at the arrival of each leg.
- rrd   : Matrix of position vectors at the departure of each leg.
- rra   : Matrix of position vectors at the arrival of each leg.

## Function Signature
```matlab
[VINFS, vvd, vva, rrd, rra] = path2Vinfs(path, idcentral, customEphemerides)
```
