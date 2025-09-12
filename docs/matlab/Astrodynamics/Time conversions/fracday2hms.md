# `fracday2hms`

## DESCRIPTION:
Converts the fraction of day to hours, minutes, and seconds.

## INPUT:
fracDay[1] A single real greater or equal to 0 and strictly lower than
1.

## OUTPUT:
hrs[1]     Number of hours as integer greater or equal to 0 and lower
or equal to 23.
mn[1]      Number of minutes as integer greater or equal to 0 and
lower or equal to 59.
sec[1]     Number of seconds as a real greater or equal to 0 and
strictly lower than 60.
See also hms2fracday.
CALLED FUNCTIONS:
(none)
AUTHOR:
Nicolas Croisard, 16/02/2008, MATLAB, fracday2hms.m
CHANGELOG:
21/02/2008, REVISION, Matteo Ceriotti
22/04/2010, Camilla Colombo: Header and function name in accordance
with guidlines.

## Function Signature
```matlab
[hrs, mn, sec] = fracday2hms(fracDay)
```
