# `EphCA_car`

## INPUTS:
n: ID of the comet. [ND]
t: epoch at which the ephemerides should be computed. [MJD2000]

## OUTPUTS:
rr: vector [1x3] containing position of the comet. [km]
vv: vector [1x3] containing velocity of the comet. [km/s]
kep: keplerian elements for the comet. [sma, ecc, incl, Om, om, th]
(it can be added as output).
NOTE: All the inputs required by the user are designed as 'user input'.
Functions used:
propagateKepler.m
car2kep.m
Author:
Andrea Bellome (main structure).
Jose Ignacio Rico Alvarez (modifications to apply the code
for all the considered comets).
History of modifications:
Creation date: 18 - June - 2021

## Function Signature
```matlab
[rr, vv, kep] = EphCA_car(n, t)
```
