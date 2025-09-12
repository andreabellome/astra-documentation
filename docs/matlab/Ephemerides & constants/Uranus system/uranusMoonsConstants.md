# `uranusMoonsConstants`

## DESCRIPTION
This function extracts physical and orbital parameters of main Uranus
moons.

## INPUT
- idMO : moon ID (1. Miranda, 2. Ariel, 3. Umbriel, 4. Titania, 5. Oberon)

## OUTPUT
- rcm  : circular orbit radius of the body [km]
- mum  : gravitational parameter of the body [km3/s2]
- radm : circular radius of the body [km]
- hmin : minimum altitude for the flyby [km]

## Function Signature
```matlab
[rcm, mum, radm, hmin] = uranusMoonsConstants(idMO)
```
