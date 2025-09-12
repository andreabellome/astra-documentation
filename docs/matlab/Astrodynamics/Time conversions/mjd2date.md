# `mjd2date`

## INPUT
mjd         Date in modified Julian Day. The MJD count is from 00:00
midnight at the beginning of Wednesday November 17, 1858.
It must be a real greater or equal than -2400000.5.

## OUTPUT
date        Date in the Gregorian calendar, as a 6-element vector
[year, month, day, hour, minute, second]. For dates before
1582, the resulting date components are valid only in the
Gregorian proleptic calendar. This is based on the
Gregorian calendar but extended to cover dates before its
introduction.
See also DATE2MJD.
FUNCTIONS CALLED
MJD2JD
JD2DATE
- Nicolas Croisard - 16/02/2008
- Revised by Matteo Ceriotti - 21/02/2008

## Function Signature
```matlab
[date] = mjd2date(mjd)
```
