# `saveOUTPUT_MODP`

## DESCRIPTION
This function saves the output results of a multi-objective optimization problem,
including details of the optimal trajectory, associated costs, and other relevant metrics.

## INPUT
- LEGSnext  : Matrix containing the legs of the trajectory for each candidate solution.
- VASnext   : Matrix containing the velocity vectors associated with the trajectory legs.
- VINFnext  : Matrix containing the hyperbolic excess velocity vectors for each leg.
- INPUT     : Struct containing various input parameters, including the cost function.
- runOpts   : Matrix containing run-time options for the optimization process.
- chosenRev : Vector indicating the chosen number of revolutions for each leg.
- tocTOT    : Total elapsed time for the optimization process.

## OUTPUT
- OUTPUT    : Struct containing all relevant outputs of the optimization process.
This includes information about the Pareto front, the minimum cost path,
and additional metrics for performance analysis.

## Function Signature
```matlab
[OUTPUT] = saveOUTPUT_MODP(LEGSnext, VASnext, VINFnext, INPUT, runOpts, chosenRev, tocTOT)
```
