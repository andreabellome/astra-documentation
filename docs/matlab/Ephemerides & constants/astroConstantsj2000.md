# `astroConstantsj2000`

## DESCRIPTION
This function retrieves astronomical constants for a specified planet
in the Solar System. It provides the planet's distance from the Sun
(semi-major axis), gravitational parameter, and radius. If the specified
planet is not available in the pre-defined list, it attempts to calculate
the distance using ephemerides data.

## INPUT
- pl    : Planet index (1 for Mercury, 2 for Venus, ..., 8 for Neptune)

## OUTPUT
- r     : Distance from the Sun (semi-major axis) in kilometers.
- radPL : Radius of the planet in kilometers.
- muPL  : Gravitational parameter of the planet in km^3/s^2.

## Function Signature
```matlab
[r, radPL, muPL] = astroConstantsj2000(pl)
```
