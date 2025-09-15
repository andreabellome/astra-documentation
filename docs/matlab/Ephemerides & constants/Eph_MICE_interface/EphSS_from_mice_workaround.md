# `EphSS_from_mice_workaround`

## DESCRIPTION
This function is a workaround for getting ephemerides from NASA MICE
toolbox.

## INPUT
- IDspk       : SPK id of the desired body
- t           : epoch in MJD2000
- idcentral   : ID of the central body (see constants.m)

## OUTPUT
- rr : Cartesian position vector of the celestial body (3x1 vector).
- vv : Cartesian velocity.

## Function Signature
```matlab
[rr, vv] = EphSS_from_mice_workaround(IDspk, t, idcentral)
```
