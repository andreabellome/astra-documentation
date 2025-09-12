# `plotLT_Th`

## DESCRIPTION
This function generates a plot of the thrust magnitude over time for a
low-thrust trajectory. The plot can either create a new figure or overlay
the data onto an existing figure, depending on the input argument 'holdon'.

## INPUT
- transfer : matrix containing trajectory data (see also plotLT.m)
- param    : structure containing parameters for the plot. For example,
'rho' is used in the plot legend to label the curve.
- holdon   : optional binary input. If set to 0 (default), a new figure is
created for the plot. If set to 1, the plot is overlaid onto
the current figure.
- name     : optional string input. This is the name of the curve for the
legend display.

## OUTPUT
- figTHRmag : handle to the figure containing the thrust magnitude plot.

## Function Signature
```matlab
[figTHRmag] = plotLT_Th( transfer, param, holdon, name )
```
