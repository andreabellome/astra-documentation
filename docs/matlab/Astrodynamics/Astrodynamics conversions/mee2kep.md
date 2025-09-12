# `mee2kep`

## DESCRIPTION
This function converts a vector of Modified Equinoctial Elements (MEE) to
the equivalent set of Classical Orbital Elements (COE).

## INPUT
- mee : 6x1 vector of Modified Equinoctial Elements [p, f, g, h, k, L], where:
- p : semi-latus rectum [km]
- f : e*cos(omega + Omega)
- g : e*sin(omega + Omega)
- h : tan(i/2)*cos(Omega)
- k : tan(i/2)*sin(Omega)
- L : true longitude [rad]

## OUTPUT
- kep : 1x6 vector of Classical Orbital Elements [a, e, i, RAAN, ω, θ], where:
- a     : semi-major axis [km]
- e     : eccentricity
- i     : inclination [rad]
- Omega : right ascension of ascending node [rad]
- omega : argument of pericenter [rad]
- theta : true anomaly [rad]

## Function Signature
```matlab
[kep] = mee2kep(mee)
```
