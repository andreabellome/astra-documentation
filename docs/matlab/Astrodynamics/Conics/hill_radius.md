# `hill_radius`

## DESCRIPTION
This function computes the Hill radius of a secondary body orbiting a
central body. The Hill radius represents the region around the secondary
body where its gravitational influence dominates over the tidal forces of
the central body. If the central body is Earth (ID 1) and the secondary
body is the Sun (ID 3), the mass of the Moon is also included in the
calculation.

## INPUT
- idcentral       : integer identifier of the central body
- secondary_body  : integer identifier of the secondary body

## OUTPUT
- r_hill         : Hill radius of the secondary body [km]

## Function Signature
```matlab
[r_hill] = hill_radius( idcentral, secondary_body )
```
