# `saveOUTPUT_SODP`

## DESCRIPTION:
This function saves various results from a space mission optimization process.
It handles cases where no solutions are found and where solutions are available.
It computes and saves the Pareto front, minimum cost path, and additional information.

## INPUT
runOpts    : Options for running the mission optimization.
chosenRev  : Vector of chosen revision options.
tocTOT     : Total time of computation.

## INPUTS:
LEGSnext   : Matrix of the next leg configurations.
VASnext    : Matrix of the velocities associated with the next leg configurations.
VINFnext   : Matrix of the inertias associated with the next leg configurations.

## Function Signature
```matlab
[OUTPUT] = saveOUTPUT_SODP(LEGSnext, VASnext, VINFnext, INPUT, runOpts, chosenRev, tocTOT)
```
