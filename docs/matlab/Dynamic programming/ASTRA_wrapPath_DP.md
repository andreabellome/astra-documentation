# `ASTRA_wrapPath_DP`

## DESCRIPTION
this function allows for building the path matrix of an MGA sequence.

## INPUT
seq   : vector with planets IDs in the MGA sequence
t0    : departing epoch (MJD2000)
tofs  : vector with time of fligth for each leg of the sequence (days)
NREVS : nx3 matrix (n=length(seq)-1) on which the multiple revolutions
options are passed. If NREVS(i,3)~=0, then a resonance is
included in the transfer.
idcentral  : ID of the central body. See constants.m
customEphemerides : user-defined custom ephemerides. See EphSS_cartesian.m to define those

## OUTPUT
path : is the path matrix
fig  : if requested by the user, a figure with the trajectory is returned

## Function Signature
```matlab
[path, fig] = ASTRA_wrapPath_DP(seq, t0, tofs, NREVS, idcentral, customEphemerides)
```
