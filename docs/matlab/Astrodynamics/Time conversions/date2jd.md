# `date2jd`

## DESCRIPTION:
Returns the Julian day number of the given date (Gregorian calendar)
plus a fractional part depending on the time of day.
Note: The function is valid for the whole range of dates since 12:00
noon 24 November -4713, Gregorian calendar. (This bound is set in
order to have symmetry with the inverse function jd2date.m)
Note: The inputs must be feasible (i.e. the date must exist!). If an
unfeasible date is inputed, wrong results are given because no
check is done on that.

## INPUT:
date[6]     Date in the Gregorian calendar, as a 6-elements vector
[year, month, day, hour, minute, second]. For dates before
1582, the resulting date components are valid only in the
Gregorian proleptic calendar. This is based on the
Gregorian calendar but extended to cover dates before its
introduction. Date must be after 12:00 noon, 24 November
-4713.

## OUTPUT:
jd[1]       Date in Julian Day. The JD (Julian day) count is from 0 at
12:00 noon, 1 January -4712 (4713 BC), Julian proleptic
calendar. The corresponding date in Gregorian calendar is
12:00 noon, 24 November -4713.
REFERENCES:
Formula from http://scienceworld.wolfram.com/astronomy/JulianDate.html
(last visited 15/02/2008)
Compared to http://pdc.ro.nu/mjd.cgi for a few dates, the same results
were found
See also JD2DATE.
CALLED FUNCTIONS
hms2fracday
AUTHOR:
Nicolas Croisard, 16/02/2008, MATLAB, date2jd.m
CHANGELOG:
03/03/2008, REVISION: Camilla Colombo
22/04/2010, Camilla Colombo: Header and function name in accordance
with guidlines.

## Function Signature
```matlab
[jd] = date2jd(date)
```
