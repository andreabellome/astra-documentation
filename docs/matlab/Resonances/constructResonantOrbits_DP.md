# `constructResonantOrbits_DP`

## DESCRIPTION
This function constructs resonant orbits for a spacecraft by evaluating potential
trajectories that satisfy a specified resonance condition with a planet. It computes
the spacecraft's incoming and outgoing velocities during a planetary flyby and
determines if a resonant orbit can be achieved while minimizing the change in
orbital inclination.

## INPUT
- legp    : Row vector containing the current leg information of the spacecraft's trajectory.
- vasp    : Row vector of the spacecraft's velocity corresponding to the current leg.
- vinfp   : Row vector of the spacecraft's hyperbolic excess velocity for the current leg.
- plt     : ID of the planet involved in the resonance.
- res     : Array specifying the desired resonance [numerator, denominator].
- tolINCL : Tolerance for the inclination change between the incoming and outgoing orbit.
- parallel: Boolean flag indicating if parallel processing is used (not used in this function).

## OUTPUT
- legn    : Matrix containing the legs of the spacecraft's trajectory after constructing
the resonant orbits. Empty if no valid orbit is found.
- vasn    : Matrix of spacecraft velocities after constructing resonant orbits.
Empty if no valid orbit is found.
- vinfn   : Vector of spacecraft's hyperbolic excess velocities after constructing resonant orbits.
Empty if no valid orbit is found.
- MAT_VV  : Matrix containing various parameters of the evaluated orbits, including
incoming/outgoing velocities and inclination change.

## Function Signature
```matlab
[legn, vasn, vinfn, MAT_VV] = constructResonantOrbits_DP(legp, vasp, vinfp, plt, res, tolINCL, idcentral, customEphemerides)
```
