# `apses_velocities`

## DESCRIPTION
This function computes the velocities at periapsis and apoapsis for an
orbit given the periapsis radius, apoapsis radius, and standard
gravitational parameter. It also calculates the semi-major axis,
eccentricity, and orbital period.

## INPUT
- rp : periapsis radius (scalar, in consistent length units)
- ra : apoapsis radius (scalar, in consistent length units)
- mu : standard gravitational parameter (scalar, in consistent units)

## OUTPUT
- vp     : velocity at periapsis (scalar, in consistent velocity units)
- va     : velocity at apoapsis (scalar, in consistent velocity units)
- sma    : semi-major axis of the orbit (scalar, in consistent length units)
- ecc    : eccentricity of the orbit (scalar, dimensionless)
- period : orbital period (scalar, in consistent time units)

## Function Signature
```matlab
[vp, va, sma, ecc, period] = apses_velocities( rp, ra, mu )
```
