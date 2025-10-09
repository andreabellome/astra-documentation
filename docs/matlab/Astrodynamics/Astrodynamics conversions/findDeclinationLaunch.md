# `findDeclinationLaunch`

## DESCRIPTION
This function computes the declination and right ascension of the
asymptotic velocity vector at launch, given the heliocentric velocity
vectors of the spacecraft and the planet at departure.

## INPUT
- vvsc : spacecraft heliocentric velocity vector [1x3] [km/s]
- vvpl : planet heliocentric velocity vector at departure [1x3] [km/s]

## OUTPUT
- Dec : declination of the launch asymptote [rad]
- Asc : right ascension of the launch asymptote [rad]

## Function Signature
```matlab
[Dec, Asc] = findDeclinationLaunch(vvsc, vvpl)
```
