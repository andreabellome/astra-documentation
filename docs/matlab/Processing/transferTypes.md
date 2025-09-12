# `transferTypes`

## DESCRIPTION
given a path from ASTRA output, find the transfer types (OO, OI, IO, II).

## INPUT
- path      : MGA transfer as coming from ASTRA outputù
- idcentral : ID of the central body

## OUTPUT
- TYPES  : matrix containing the follwing info :
- TYPES(:,1) : departing planet
- TYPES(:,2) : arrival planet
- TYPES(:,3:4) : transfer type (88=OO, 81=OI, 18=IO, 11=II)
- STATES : matrix containing the following info :
- STATES(:,1)    : departing planet
- STATES(:,2)    : arrival planet
- STATES(:,3:8)  : SC state after the flyby with the dep. planet
- STATES(:,9:14) : SC state after the flyby with the arr. planet

## Function Signature
```matlab
[TYPES, STATES, fig] = transferTypes(path, idcentral)
```
