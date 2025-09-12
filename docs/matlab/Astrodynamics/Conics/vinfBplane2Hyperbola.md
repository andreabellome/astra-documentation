# `vinfBplane2Hyperbola`

## DESCRIPTION
This function computes the hyperbola parameters given B-plane parameters.

## INPUT
- vinf_bplane_params : 1x6 vector with the following parameters
- vinf_mag        = vinf_bplane_params(1) magnitude
of infinity velocity [km/s]
- right_ascension = vinf_bplane_params(2) right
ascension of the infinity velocity vector [rad] -->
NOT USED!!! Can be NaN.
- declination     = vinf_bplane_params(3)
declination of the infinity velocity vector [rad]
--> NOT USED!!! Can be NaN.
- bt              = vinf_bplane_params(4) BT
component of the B-vector [km]
- br              = vinf_bplane_params(5) BR
component of the B-vector [km]
- th              = vinf_bplane_params(6) true
anomaly along the hyperbola [rad] --> NOT USED!!!
Can be NaN.

## OUTPUT
- delta : hyperbolic deflection (rad)
- vpip  : hyperbolic pericentre velocity (km/s)
- eip   : hyperbolic eccentricity
- Eip   : hyperbolic energy (km2/s2)
- aip   : hyperbolic semi-major axis (a<0) (km)

## Function Signature
```matlab
[delta, vpip, eip, Eip, aip] = vinfBplane2Hyperbola(vinf_bplane_params, mu_planet)
```
