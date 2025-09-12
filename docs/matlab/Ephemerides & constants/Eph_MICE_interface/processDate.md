# `processDate`

## DESCRIPTION
This function converts an input time expressed in Modified Julian Date
2000 (MJD2000) into a formatted date string compatible with the NASA
NAIF MICE Toolkit. It is primarily used for trajectory design problems
involving multiple gravity assists.

## INPUT
- t    : time in Modified Julian Date 2000 (MJD2000)

## OUTPUT
- date : formatted date string 'YYYY MM DD HH.mmssssssss' (TDB time scale)
to be passed to SPICE functions such as cspice_str2et

## Function Signature
```matlab
[date] = processDate(t)
```
