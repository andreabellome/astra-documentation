# `satMoonsConstants`

## DESCRIPTION
This function extracts physical and orbital parameters of main Saturn
moons.

## INPUT
- idMO : moon ID (0. Mimas, 1. Enceladus, 2. Tethys, 3. Dione, 4. Rhea, 5. Titan)

## OUTPUT
- rcm  : circular orbit radius of the body [km]
- mum  : gravitational parameter of the body [km3/s2]
- radm : circular radius of the body [km]
- hmin : minimum altitude for the flyby [km]

## Function Signature
```matlab
[rcm, mum, radm, hmin] = satMoonsConstants(idMO)
```
