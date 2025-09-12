# `EphSS_car`

## DESCRIPTION:
It uses uplanet for planets, moon_eph for the Moon, and NeoEphemeris
for asteroid ephemerides. Outputs cartesian position and velocity of
the body, centered in the Sun for all the bodies but the Moon (for
which a cartesian Earth-centered reference frame is chosen).

## INPUT:
n[1]	ID of the body:
1 to 9: Planets
t[1]    Time [d, MJD2000]. That is:
modified Julian day since 01/01/2000, 12:00 noon
(MJD2000 = MJD-51544.5)

## OUTPUT:
r[1,3]  Cartesian position of the body (Sun-centered for all bodies).
v[1,3]  Cartesian velocity.

## Function Signature
```matlab
[r,v,kep] = EphSS_car(n,t)
```
