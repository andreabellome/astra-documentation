# `hms2fracday`

## INPUT
hrs        Number of hours as integer greater or equal to 0 and lower
or equal to 23.
mn         Number of minutes as integer greater or equal to 0 and
lower or equal to 59.
sec        Number of seconds as a real greater or equal to 0 and
strictly lower than 60.

## OUTPUT
fracDay    A single real greater or equal to 0 and strictly lower than
1.
See also FRACDAY2HMS.
FUNCTIONS CALLED
none
- Nicolas Croisard - 16/02/2008
- Revised by Camilla Colombo - 29/02/2008

## Function Signature
```matlab
[fracDay] = hms2fracday(hrs, mn, sec)
```
