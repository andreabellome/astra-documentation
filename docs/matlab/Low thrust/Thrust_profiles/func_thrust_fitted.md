# `func_thrust_fitted`

## DESCRIPTION
Smooth Solar Electric Propulsion (SEP) thrust profile (see also
func_thrust_true.m)

## INPUT:
- dist_to_sun_au : Sun-spacecraft distance [AU]
- thrustParam    : structure with the following fields:
- Tmax          : max. thrust at 1 AU [N] (e.g., 1.05 N)
- n_engines     : number of engines
- thrust_max_N  : reference thrust for each engine [N]
(e.g., 0.255 N)
- epsilon       : smooth factor for the thrust profile
(by default 0.002)

## OUTPUT:
- thrust_profile : thrust magnitude w.r.t. the Sun-spacecraft distance [N]

## Function Signature
```matlab
[thrust_profile] = func_thrust_fitted( dist_to_sun_au, thrustParam )
```
