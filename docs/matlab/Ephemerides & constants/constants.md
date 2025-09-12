# `constants`

## DESCRIPTION
This function extracts central body and flyby body parameters. It assumes
circular coplanar orbits of the flyby bodies around the central body.
Each flyby body is assumed to be a perfect sphere.

## INPUT
- idcentral : ID of the central body
1:  Sun
30: Earth
5:  Jupiter
6:  Saturn
7:  Uranus
- pl        : ID of the flyby body, depending on the idpl
if idcentral = 0:
flyby body ID (1. Mercury, 2. Venus, 3. Earth, 4. Mars, 5. Jupiter, ...
6. Saturn, 7. Uranus, 8. Neptune)
if idcentral = 30
flyby body ID (0. Moon)
if idcentral = 5
flyby body ID (1. Io, 2. Europa, 3. Ganimede, 4. Callisto)
if idcentral = 6
flyby body ID (0. Mimas, 1. Enceladus, 2. Tethys, 3. Dione, 4. Rhea, 5. Titan)
if idcentral = 7
flyby body ID (1. Miranda, 2. Ariel, 3. Umbriel, 4. Titania, 5. Oberon)

## OUTPUT
- muCentral : gravitational parameter of the central body [km3/s2]
- mupl      : gravitational parameter of the flyby body [km3/s2]
- rpl       : circular orbit radius of the flyby body [km]
- radpl     : circular radius of the flyby body [km]
- hmin      : minimum altitude for the flyby [km]
- Tpl       : orbital period of the flyby body [s]

## Function Signature
```matlab
[muCentral, mupl, rpl, radpl, hmin, Tpl] = constants(idcentral, pl)
```
