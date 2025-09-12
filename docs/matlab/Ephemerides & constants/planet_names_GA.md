# `planet_names_GA`

## DESCRIPTION
This function gives strings with intials and full names of flyby bodies
depending upon the selected system (see also constants.m).

## INPUT
- planet_id : ID of the flyby body (see also constants.m)
- idcentral : ID of the central body (see also constants.m)

## OUTPUT
- planet     : string with initial letter for the flyby body
- fullName   : string with full name of the flyby body
- cenralName : string with full name of the central body

## Function Signature
```matlab
[planet, fullName, cenralName] = planet_names_GA(planet_id, idcentral)
```
