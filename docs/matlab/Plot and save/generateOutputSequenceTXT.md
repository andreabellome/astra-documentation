# `generateOutputSequenceTXT`

## DESCRIPTION
This function generates a textual representation of a sequence of planets
from a given trajectory path by converting each planet ID to a corresponding
symbol or name.

## INPUT
- path   : Matrix where each row represents a state in the trajectory
with the 7th column indicating the planet ID.

## OUTPUT
- sequence : A string representing the sequence of planets in the trajectory,
where each planet ID is replaced by a specific symbol or name.

## Function Signature
```matlab
[sequence] = generateOutputSequenceTXT(path, idcentral)
```
