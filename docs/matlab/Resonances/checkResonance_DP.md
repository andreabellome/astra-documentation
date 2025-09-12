# `checkResonance_DP`

## DESCRIPTION
This function checks if specific resonances can be achieved during a spacecraft's flyby
based on the provided resonance ratio. It evaluates the feasibility of resonant orbits
by calculating the spacecraft's post-flyby trajectory and comparing it with the
required conditions for resonance.

## INPUT
- LEGSnext : Matrix containing the legs of the spacecraft's trajectory, where each row
corresponds to a different leg.
- VASnext  : Matrix containing the spacecraft's velocities corresponding to each leg.
- VINFnext : Matrix containing the hyperbolic excess velocities for each leg.
- plt      : Identifier for the planet the flyby is around.
- res      : Array containing the desired resonance ratio [numerator, denominator].
- parallel : Boolean flag to indicate whether to run the resonance checks in parallel.

## OUTPUT
- LEGSnext : Updated matrix of legs after filtering out those that cannot achieve resonance.
- VASnext  : Updated matrix of velocities after filtering.
- VINFnext : Updated matrix of hyperbolic excess velocities after filtering.

## Function Signature
```matlab
[LEGSnext, VASnext, VINFnext] = checkResonance_DP(LEGSnext, VASnext, VINFnext, plt, res, parallel, idcentral, customEphemerides)
```
