# `planetIdToName`

## DESCRIPTION
This function converts a planet ID to its corresponding planet name. The planet IDs
are mapped to their respective names using a predefined list of planet names. If the
provided ID is out of the expected range, the function returns the ID as a string.

## INPUT
- idPL : Integer representing the ID of the planet (1 for Mercury, 2 for Venus, etc.).
- idcentral : ID of the central body. See constants.m

## OUTPUT
- name : String containing the name of the planet corresponding to the given ID.
If the ID is out of range, the function returns the ID itself as a string.

## Function Signature
```matlab
[name] = planetIdToName(idPL, idcentral)
```
