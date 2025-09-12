# `mee2kep`

## DESCRIPTION
This function converts a vector of Modified Equinoctial Elements (MEE) to
the equivalent set of Classical Orbital Elements (COE).

## INPUT
- mee : 6x1 vector of Modified Equinoctial Elements [p, f, g, h, k, L], where:
p : semi-latus rectum
f : component of eccentricity vector along x
g : component of eccentricity vector along y
h : component of inclination vector along x
k : component of inclination vector along y
L : true longitude

## OUTPUT
- kep : 1x6 vector of Classical Orbital Elements [a, e, i, RAAN, ω, θ], where:
a    : semi-major axis
e    : eccentricity
i    : inclination
RAAN : right ascension of ascending node
ω    : argument of periapsis
θ    : true anomaly

## Function Signature
```matlab
[kep] = mee2kep(mee)
```
