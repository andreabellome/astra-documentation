# `EphSS_cartesian`

## DESCRIPTION:
This function computes the Cartesian position (rr) and velocity (vv) vectors for a given celestial body at a specific time.
It uses different ephemeris functions depending on the type of body, such as planets, asteroids, or other objects.

## INPUT:
- pl : Identifier for the celestial body.
- Values <= 10 correspond to planets in the Solar System.
- Values between 11 and 473 correspond to Jupiter-family comets.
- Values between 474 and 1183 correspond to Centaurs.
- Value 1194 corresponds to the asteroid Lutetia.
- Other values are handled by a default ephemeris function.
- t          : Time at which the position and velocity vectors are to be computed.
- idcentral  : ID of the central body. See constants.m

## OUTPUT:
- rr : Cartesian position vector of the celestial body (3x1 vector).
- vv : Cartesian velocity vector of the celestial body (3x1 vector).

## Function Signature
```matlab
[rr, vv] = EphSS_cartesian(pl, t, idcentral)
```
