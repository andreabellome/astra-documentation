# `plotPath`

## DESCRIPTION
This function plots the trajectory of a spacecraft and the orbits of
planets along with various related plots. The spacecraft's trajectory
is based on the provided path data, which includes the state vectors at
different time points. The function also generates plots in both the
ECI (Earth-Centered Inertial) and Synodic reference frames, as well as
plots of distance and velocity over time.

## INPUT
- path      : Nx8 matrix where each row contains the state vector of the
spacecraft at a given time. Columns represent position and
velocity in ECI frame, as well as time and planet IDs.
- idcentral : ID of the central body. See constants.m
- customEphemerides : user-defined custom ephemerides. See EphSS_cartesian.m for reference
- holdon    : optional flag to determine if the current figure should be
held for additional plotting. Default is 0 (create new figure).
- color     : optional color for the trajectory plot. Default is 'b' (blue).
- firstL    : optional flag to highlight the departure condition. Default
is 1 (highlight).

## OUTPUT
- figECI : handle to the figure showing the spacecraft trajectory and
planets' orbits in the ECI frame.
- STRUC  : structure containing trajectory and planet data including:
- StatesSC : spacecraft states in ECI frame
- EpochsSC : time epochs corresponding to spacecraft states
- TOFsSC   : time of flight between waypoints
- DistSC   : distance from the Sun over time
- VelSC    : spacecraft velocity over time
- SatesScFB : state vectors at flyby points
- EpochsScFB : epochs of flyby points
- Planets  : structure array of planets' states in the ECI and
Synodic frames
- figSYN : handle to the figure showing the spacecraft trajectory and
planets' orbits in the Synodic frame.
- figRSC : handle to the figure showing the distance from the Sun over
time.
- figVSC : handle to the figure showing the spacecraft velocity over time.

## Function Signature
```matlab
[figECI, STRUC, figSYN, figRSC, figVSC] = plotPath(path, idcentral, customEphemerides, holdon, color, firstL)
```
