# `approxEphemJupMoons_cc`

## DESCRIPTION
This function provides an approximation of the ephemerides for Jupiter's
moons (Io, Europa, Ganymede, and Callisto) using Keplerian elements.
It is intended for use in Delta-V (DV) and time of flight (TOF) analyses
but not for mission design purposes.

## INPUT
- idmoon : Integer identifier for the Jupiter moon:
1 --> Io
2 --> Europa
3 --> Ganymede
4 --> Callisto
- t      : Time of interest in Modified Julian Date (MJD2000).

## OUTPUT
- rr     : Position vector of the moon at time t (in kilometers).
- vv     : Velocity vector of the moon at time t (in kilometers per second).
- kep    : Keplerian elements of the moon at time t.

## PROCESS
- Defines reference epoch and initial Keplerian elements for each moon.
- Computes the position and velocity vectors by propagating the initial
Keplerian elements to the given time using the FGKepler_dt function.

## Function Signature
```matlab
[rr, vv, kep] = approxEphemJupMoons_cc(idmoon, t)
```
