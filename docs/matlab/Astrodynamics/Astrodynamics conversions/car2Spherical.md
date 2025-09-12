# `car2Spherical`

## DESCRIPTION
Spherical coordinates (r, th, phi) to position vector (pos_x, pos_y,
pos_z).

## INPUT
- cart : position vector (pos_x, pos_y, pos_z)

## OUTPUT
- spherical : 1x3 spherical coordinates such that :
- spherical(1) is the radius
- spherical(2) is the azimuth
- spherical(3) is the elevation

## Function Signature
```matlab
[spherical] = car2Spherical( cart )
```
