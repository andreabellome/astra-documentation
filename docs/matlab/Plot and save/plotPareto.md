# `plotPareto`

## DESCRIPTION
This function plots the Pareto front of solutions on a 2D plot, with the x-axis representing
time of flight (in years) and the y-axis representing delta-v (in km/s). The plot can be
customized with various input arguments to hold the plot, change markers, colors, and add labels.

## INPUT
- paretofront : Matrix where each row represents a point on the Pareto front, with the first
column being the time of flight and the second column being the delta-v.
- holdon      : Boolean flag to determine whether to hold the current plot or create a new one.
If holdon == 1, the current plot is held; otherwise, a new plot is created.
- marker      : String specifying the marker type for the plot points (e.g., 'o', 'x').
- color       : String or RGB triplet specifying the color of the plot markers.
- name        : String specifying the name to be used in the legend for this Pareto front.
- markersize  : Scalar value specifying the size of the plot markers.

## OUTPUT
- fig : Handle to the created or modified figure.

## Function Signature
```matlab
[fig] = plotPareto(paretofront, holdon, marker, color, name, markersize)
```
