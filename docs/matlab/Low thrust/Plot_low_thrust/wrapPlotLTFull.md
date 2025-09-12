# `wrapPlotLTFull`

## DESCRIPTION
This function generates trajectory plots for a low-thrust transfer, including
mass and thrust magnitude plots. It calls the plotLT function to generate
the primary plots and overlays initial and final states on the trajectory plot.

## INPUT
- LT_SOLUTION : structure containing low-thrust transfer data for all the
legs of an MGA transfer
- param : structure containing parameters

## OUTPUT
- figTRAJ   : figure handle for the trajectory plot
- figMASS   : figure handle for the mass evolution plot
- figTHRmag : figure handle for the thrust magnitude plot

## Function Signature
```matlab
[figTRAJ, figMASS, figTHRmag] = wrapPlotLTFull(LT_SOLUTION, param)
```
