# `wrapECI2Synodic_SE`

## INPUT
- statesECI : (Nx6) [rr, vv] state vectors in eclipticJ2000 frame taken
at different epochs (km, km/s)
- epochs    : (Nx1) epochs at which the state vectors are computed
(MJD2000)
- idcentral : ID of the central body. See constants.m

## OUTPUT
- statesSYN : (Nx6) [rr, vv] state vectors in Sun-Earth Synodic frame
taken at the same epochs (Lref, Vref)

## Function Signature
```matlab
[statesSYN] = wrapECI2Synodic_SE(statesECI, epochs, idcentral, customEphemerides, pl)
```
