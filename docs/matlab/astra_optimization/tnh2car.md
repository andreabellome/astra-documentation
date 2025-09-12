# `tnh2car`

## DESCRIPTION:
Transformation from tangential-normal-h to Cartesian reference frame.
Tangential-normal-h (tnh) reference frame: {t,n,h}
t-axis: direction tangent to the motion.
h-axis: direction of the angular momentum.
n-axis: direction in the orbit plane, normal to t (inward).
Cartesian (car) reference frame: {x,y,z}
inertial reference frame.
Note: other definition use the {t,h,n} reference frame, where n is
outward!

## INPUT:
x_tnh[3]    Vector to be transformed, expressed in {t,n,h}.
s_car[6]    State vector (position [L], velocity [L/T]) of the orbiting
body, expressed in {x,y,z}.

## OUTPUT:
x_car[3,1]  Vector transformed into {x,y,z}.
EXAMPLE:
Given a spacecraft in orbit:
- we have the thrust vector in {t,n,h};
- we want the thrust vector in {x,y,z}.
In this case:
x_rth = Thrust vector in {t,n,h};
s_car = [position, velocity] of the spacecraft in {x,y,z};
x_car = Thrust vector, transformed in {x,y,z}.
CALLED FUNCTIONS:
crossFast
AUTHOR:
Camilla Colombo, 03/03/2006, MATLAB, tnh2car.m
PREVIOUS VERSION:
Camilla Colombo, 03/03/2006, MATLAB, tnh_carT.m
- Header and function name in accordance with guidlines.
CHANGELOG:
10/01/2007, REVISION: Matteo Ceriotti
11/02/2008, Matteo Ceriotti: Help improved.
30/09/2009, Camilla Colombo: Header and function name in accordance
with guidlines.
29/03/2010, Camilla Colombo: crossFast used.

## Function Signature
```matlab
[x_car, A] = tnh2car(x_tnh,s_car)
```
