# `approxEphemSatMoons_cc`

## DESCRIPTION
Approximate ephemerides of Saturn moons, assumed to be in circular
coplanar orbits around Saturn. The reference epoch is 2030-01-01.

## INPUT
- idmoon :
- t      : epoch at which the ephemerides are computed [MJD2000]

## OUTPUT
- rr  : 1x3 vector with moon position [km]
- vv  : 1x3 vector with moon velocity [km]
- kep : 1x6 vector with keplerian elements (see car2kep.m)

## Function Signature
```matlab
[rr, vv, kep] = approxEphemSatMoons_cc(idmoon, t)
```
