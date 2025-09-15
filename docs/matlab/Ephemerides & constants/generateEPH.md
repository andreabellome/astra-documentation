# `generateEPH`

## DESCRIPTION:
This function generates an ephemeris matrix by computing the Cartesian position and velocity vectors for each
time pair in the provided matrix. The result includes both the input time pairs and the computed vectors.

## INPUT:
- M                 : Matrix where each row contains a time pair with the format [planet ID, time]. The matrix represents either
departure or arrival times.
- idcentral         : ID of the central body. See constants.m
- customEphemerides : user-defined custom ephemerides. See EphSS_cartesian.m for reference

## OUTPUT:
- EPH : Matrix where each row includes the original time pair followed by the Cartesian position (rr) and velocity (vv) vectors.
The matrix has 8 columns in total: [planet ID, time, rr (3 columns), vv (3 columns)].

## Function Signature
```matlab
[EPH] = generateEPH(M, idcentral, customEphemerides)
```
