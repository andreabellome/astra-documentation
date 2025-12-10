# `vinfVec2VinfBplane`

## DESCRIPTION:
This function computes the v-infinity B-plane parameters and the
periapsis radius from an incoming and outgoing infinity velocities
vectors.
The true anomaly is fixed at 0 rad, thus the parameters correspond to the
pericentre of the flyby hyperbola.

## INPUT:
- vvinfIn   : 1x3 vector of incoming v-inf [km/s]
- vvinfOu   : 1x3 vector of outgoing v-inf [km/s]
- mu_planet : gravitational parameter of the flyby body [km3/s2]

## OUTPUT
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
anomaly along the hyperbola [rad]. Default: 0.
- periapsis : periapsis radius of the flyby [km]

## Function Signature
```matlab
[vinf_bplane_params, periapsis] = vinfVec2VinfBplane( vvinfIn, vvinfOu, mu_planet )
```
