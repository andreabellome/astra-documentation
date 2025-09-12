# `fromSeq2Legs`

## DESCRIPTION:
This function processes a sequence of planetary encounters, converting it into a list of trajectory legs.
It also calculates the number of legs, the number of flybys, and the total number of planets in the sequence.

## INPUT:
SEQ   : Vector representing the sequence of planetary encounters, where each element corresponds to a specific planet.

## OUTPUT:
legs  : Matrix where each row represents a trajectory leg, with the first column indicating the departure planet
and the second column indicating the arrival planet.
nlegs : Scalar representing the total number of trajectory legs.
nfbs  : Scalar representing the number of flybys, calculated as the total number of legs minus one.
nplts : Scalar representing the total number of planets in the sequence, calculated as the total number of legs plus one.

## Function Signature
```matlab
[legs, nlegs, nfbs, nplts] = fromSeq2Legs(SEQ)
```
