# `sphere_of_influence`

## DESCRIPTION
This function computes the sphere of influence (SOI) of a secondary body
orbiting a central body. The sphere of influence represents the region
where the secondary body's gravity dominates over the tidal forces of the
central body, making it the primary gravitational influence for objects
within this region.

## INPUT
- idcentral       : integer identifier of the central body
- secondary_body  : integer identifier of the secondary body

## OUTPUT
- r_soi          : Sphere of influence radius of the secondary body [km]

## Function Signature
```matlab
[r_soi] = sphere_of_influence( idcentral, secondary_body )
```
