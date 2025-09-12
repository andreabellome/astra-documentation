# `lambertMR_MEXIFY`

## DESCRIPTION
Lambert problem solution for Keplerian dynamics and for prograde orbits
only.

## INPUT
- RI    : 1x3 vector with initial position [km]
- RF    : 1x3 vector with final position [km]
- TOF   : time of flight [sec]
- MU    : gravitational parameter of the central body [km3/s2]
- Nrev  : integer number of revolutions
- Ncase : if 0, then low-energy is selected, if 1, then high energy

## OUTPUT
- VI : 1x3 vector with initial velocity [km/s]
- VF : 1x3 vector with final velocity [km/s]

## Function Signature
```matlab
[VI,VF] = lambertMR_MEXIFY(RI, RF, TOF, MU, Nrev, Ncase)
```
