# `uplanet`

## DESCRIPTION:
Planetary orbital elements are restituited in a Sun-centred ecliptic
system.
These ephemerides were succesfully compared with JPL/NAIF/SPICE
ephemerides using de405.bps.

## INPUT
-	mjd2000[1]  Time, modified Julian day since 01/01/2000, 12:00 noon
(MJD2000 = MJD-51544.5)
-	ibody[1]    Integer number identifying the celestial body (< 11)
1:   Mercury
2:   Venus
3:   Earth
4:   Mars
5:   Jupiter
6:   Saturn
7:   Uranus
8:   Neptune
9:   Pluto
10:  Sun

## OUTPUT:
-	kep[6]    	Mean Keplerian elements of date
kep = [a e i Om om theta] [km, rad]
-	ksun[1]     Gravity constant of the Sun [km^3/s^2]

## Function Signature
```matlab
[kep] = uplanet(mjd2000, ibody)
```
