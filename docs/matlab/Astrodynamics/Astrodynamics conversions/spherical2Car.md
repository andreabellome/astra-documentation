# `spherical2Car`

## DESCRIPTION
Spherical coordinates (r, th, phi) to position vector (pos_x, pos_y,
pos_z).

## INPUT
- spherical : 1x3 spherical coordinates such that :
- spherical(1) is the radius
- spherical(2) is the right ascension
- spherical(3) is the declination

## OUTPUT
- cart : position vector (pos_x, pos_y, pos_z)

## Function Signature
```matlab
[cart] = spherical2Car( spherical )
```
