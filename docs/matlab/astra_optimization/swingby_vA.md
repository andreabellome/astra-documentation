# `swingby_vA`

## DESCRIPTION
This function computes the output position and velocity vectors after a
gravity assist (swing-by) maneuver. The maneuver is modeled as an
instantaneous velocity rotation of the incoming hyperbolic excess vector
with a specified turn angle and plane orientation. The central body
ephemerides are retrieved using a default or user-defined function.

## INPUT
- rrIN              : incoming position vector at swing-by (1×3) [km]
- vvIN              : incoming velocity vector at swing-by (1×3) [km/s]
- plIN              : ID of the flyby planet (integer, see constants.m)
- tIN               : time of swing-by [TDB] (scalar, in seconds or days)
- kIN               : rotation angle defining the plane of the flyby (rad)
- rpIN              : pericenter radius of swing-by trajectory [km]
- muPLIN            : gravitational parameter of the planet [km^3/s^2]
- idcentral         : (optional) ID of the central body for ephemerides
computation (default = 1)
- customEphemerides : (optional) function handle to compute planetary
ephemerides (default = @EphSS_cartesian)

## OUTPUT
- rrOU    : output position vector after swing-by (1×3) [km]
- vvOU    : output velocity vector after swing-by (1×3) [km/s]
- vvInfIN : incoming hyperbolic excess velocity vector (1×3) [km/s]
- vvInfOU : outgoing hyperbolic excess velocity vector (1×3) [km/s]

## Function Signature
```matlab
[rrOU, vvOU, vvInfIN, vvInfOU] = swingby_vA(rrIN, vvIN, plIN, tIN, kIN, rpIN, muPLIN, idcentral, customEphemerides)
```
