# `wrap_generateEPH`

## DESCRIPTION:
This function generates a combined ephemeris matrix by generating ephemeris data for two sets of planetary time pairs,
and then combining and deduplicating the results.

## INPUT:
M1                : Matrix of unique departure time pairs, where each row contains departure planet ID and initial time.
M2                : Matrix of unique arrival time pairs, where each row contains arrival planet ID and arrival time.
idcentral         : ID of the central body. See constants.m
customEphemerides : user-defined custom ephemerides. See EphSS_cartesian.m for reference

## OUTPUT:
EPH : Combined ephemeris matrix containing unique rows of ephemeris data for both departure and arrival time pairs.
NOTES:
- `generateEPH` is a helper function that produces ephemeris data for given time pairs.
- The output matrix `EPH` is unique and ordered based on the rows to ensure no duplicates and maintain stability.

## Function Signature
```matlab
[EPH] = wrap_generateEPH(M1, M2, idcentral, customEphemerides)
```
