# `jupMoonsConstants`

## DESCRIPTION
This function extracts physical and orbital parameters of main Juoiter
moons.

## INPUT
- idMO : moon ID (1. Io, 2. Europa, 3. Ganimede, 4. Callisto)

## OUTPUT
- rcm  : circular orbit radius of the body [km]
- mum  : gravitational parameter of the body [km3/s2]
- radm : circular radius of the body [km]
- hmin : minimum altitude for the flyby [km]

## Function Signature
```matlab
[rcm, mum, radm, hmin] = jupMoonsConstants(idMO)
```
