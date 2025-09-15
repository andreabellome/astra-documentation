# `generateMAT`

## DESCRIPTION:
This function generates a matrix of possible time pairs for a given trajectory leg, based on the departure and arrival planets,
the initial times, and the time of flight constraints. It also creates matrices for unique departure and arrival time pairs.

## INPUT:
- pl1  : Integer representing the departure planet ID.
- pl2  : Integer representing the arrival planet ID.
- T0   : Vector containing the possible initial times for the trajectory legs.
- TOFS : Vector containing the possible times of flight for the trajectory legs.

## OUTPUT:
- MAT  : Matrix of possible time pairs for the trajectory legs. Each row represents a potential trajectory with columns for
departure planet ID, initial time, arrival planet ID, and arrival time.
- M1   : Matrix of unique departure time pairs (departure planet ID and initial time).
- M2   : Matrix of unique arrival time pairs (arrival planet ID and arrival time).

## Function Signature
```matlab
[MAT, M1, M2] = generateMAT(pl1, pl2, T0, TOFS)
```
