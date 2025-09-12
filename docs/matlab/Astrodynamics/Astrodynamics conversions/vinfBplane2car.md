# `vinfBplane2car`

## DESCRIPTION
This function computes the cartesian elements (pos_x, pos_y, pos_z,
vel_x, vel_y, vel_z) in a planetary-centered inertial reference frame
from the B-plane elements.
This is only valid for hyperbolic trajectories.

## INPUT
- vinf_bplane_params : 1x6 vector with the following parameters
- vinf_mag        = vinf_bplane_params(1) magnitude
of infinity velocity [km/s]
- right_ascension = vinf_bplane_params(2) right
ascension of the infinity velocity vector [rad]
- declination     = vinf_bplane_params(3)
declination of the infinity velocity vector [rad]
- bt              = vinf_bplane_params(4) BT
component of the B-vector [km]
- br              = vinf_bplane_params(5) BR
component of the B-vector [km]
- th              = vinf_bplane_params(6) true
anomaly along the hyperbola [rad]
- mu_planet : gravitational parameter of the planet [km3/s2]

## OUTPUT
- cart : 1x6 vector with (pos_x, pos_y, pos_z, vel_x, vel_y, vel_z) in
[km] and [km/s]

## Function Signature
```matlab
[cart] = vinfBplane2car( vinf_bplane_params, mu_planet )
```
