# `EphSS_from_mice`

## DESCRIPTION
This function interfaces with the NASA NAIF MICE Toolkit to extract the
position and velocity vectors of a solar system body at a given time. It
is specifically designed for multiple gravity assist trajectory design.

## INPUT
- IDspk     : SPICE ID of the body (e.g., 399 for Earth). If the ID is < 5,
the function appends '99' (e.g., 3 becomes 399) to comply with
standard NAIF object codes for planets.
- t         : epoch in Modified Julian Date 2000 (MJD2000).
- idcentral : (optional) identifier for the central body; currently only
supports value 1 (i.e., the Sun-centric frame).

## OUTPUT
- rr : 1x3 position vector [km] of the body in the ecliptic J2000 frame
- vv : 1x3 velocity vector [km/s] of the body in the ecliptic J2000 frame

## Function Signature
```matlab
[rr, vv] = EphSS_from_mice(IDspk, t, idcentral)
```
