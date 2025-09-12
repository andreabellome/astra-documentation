# `hohmann_transfer`

## DESCRIPTION
This function computes the parameters of a Hohmann transfer between two circular orbits
with radii r1 and r2 around a central body with gravitational parameter mu.
It calculates the initial and final velocities, velocity increments,
transfer time, and intermediate velocity vectors.

## INPUT
- r1 : initial orbit radius (km)
- r2 : final orbit radius (km)
- mu : gravitational parameter of the central body (km^3/s^2)

## OUTPUT
- hohmann : structure containing the following fields:
- r1   : initial orbit radius
- v1   : initial circular velocity
- rr1  : initial position vector
- vv1  : initial velocity vector
- r2   : final orbit radius
- v2   : final circular velocity
- rr2  : final position vector
- vv2  : final velocity vector
- vvd  : departure velocity after first burn
- vva  : arrival velocity before second burn
- dvv1 : velocity change vector at departure
- dvv2 : velocity change vector at arrival
- dv1  : delta-v at departure
- dv2  : delta-v at arrival
- dvt  : total delta-v required
- Tt   : transfer time (s)

## Function Signature
```matlab
[hohmann] = hohmann_transfer(r1, r2, mu)
```
