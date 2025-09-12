# `planetConstants`

## DESCRIPTION
This function extracts body parameters for Solar System planets, assuming
circular coplanar orbits of the flyby bodies around the central body.
Each body is assumed to be a perfect sphere.

## INPUT
- idPL : flyby body ID (1. Mercury, 2. Venus, 3. Earth, 4. Mars, 5.
Jupiter, 6. Saturn, 7. Uranus, 8. Neptune)

## OUTPUT
- muPL   : gravitational parameter of the body [km3/s2]
- radius : circular radius of the body [km]
- sma    : semi-major axis of the body [km]
- rpMin  : minimum periapsis radius of the body in the 2000-2100
timeframe [km]
- raMin  : minimum apoapsis radius of the body in the 2000-2100 timeframe
[km]
- hmin   : minimum altitude for the flyby [km]

## Function Signature
```matlab
[muPL, radius, sma, rpMin, raMin, hmin] = planetConstants(idPL)
```
