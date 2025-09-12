# `jd2date`

## INPUT
jd          Date in Julian Day. The JD (Julian day) count is from 0 at
12:00 noon, 1 January -4712 (4713 BC), Julian proleptic
calendar. The corresponding date in Gregorian calendar is
12:00 noon, 24 November -4713. It must be a non-negative
real.

## OUTPUT
date        Date in the Gregorian calendar, as a 6-element vector
[year, month, day, hour, minute, second]. For dates before
1582, the resulting date components are valid only in the
Gregorian proleptic calendar. This is based on the
Gregorian calendar but extended to cover dates before its
introduction.
REFERENCES
Formula from http://en.wikipedia.org/wiki/Julian_day
(last visited 16/02/2008)
Compared to http://pdc.ro.nu/mjd.cgi for a few dates, the same results
were found
See also DATE2JD.
FUNCTIONS CALLED
FRACDAY2HMS
- Nicolas Croisard - 16/02/2008
- Revised by Matteo Ceriotti - 21/02/2008 - Validated with:
- Fliegel, Van Flandern "A machine Algorithm for Processing Calendar
Dates", Communications of the ACM, 1968. Also on Wertz, "Space
Mission Analysis and Design".
- A revised version of the algorithm on Vallado, "Fundamentals of
Astrodynamics and Applications", third edition, for dates from year
1900 to year 2100.

## Function Signature
```matlab
[date] = jd2date(jd)
```
