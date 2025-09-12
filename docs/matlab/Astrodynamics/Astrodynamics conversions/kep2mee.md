# `kep2mee`

## DESCRIPTION
This function converts classical Keplerian orbital elements into Modified
Equinoctial Elements (MEE), which are non-singular for all values of
inclination and eccentricity except for exactly zero eccentricity and
retrograde equatorial orbits. The conversion is valid for elliptical and
circular orbits.

## INPUT
- kep : vector of Keplerian elements [a, e, i, Omega, omega, theta]
where:
a     : semi-major axis [km]
e     : eccentricity
i     : inclination [rad]
Omega : right ascension of ascending node [rad]
omega : argument of pericenter [rad]
theta : true anomaly [rad]

## OUTPUT
- mee : vector of Modified Equinoctial Elements [p, f, g, h, k, L]
where:
p : semi-latus rectum [km]
f : e*cos(omega + Omega)
g : e*sin(omega + Omega)
h : tan(i/2)*cos(Omega)
k : tan(i/2)*sin(Omega)
L : true longitude [rad]

## Function Signature
```matlab
[mee] = kep2mee( kep )
```
