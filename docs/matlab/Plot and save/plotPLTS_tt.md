# `plotPLTS_tt`

## DESCRIPTION
This function plots the orbits of specified planets over a given time range
and provides an option to either open a new figure or use an existing one.
It also plots the Sun's position for reference.

## INPUT
- pl     : Vector of planet IDs to plot.
- t0     : Start time for plotting (in days).
- tend   : End time for plotting (in days).
- holdon : Optional flag to determine whether to hold on to the current figure (1) or open a new one (0).
- colors : RGB triplet for the plot of the orbits. Default is black
- names  : cell with names of the planets. Default is empty. This is used
only for putting legend to the plot.

## OUTPUT
- fig   : Handle to the figure created or used for plotting.

## PROCESS
- If only three input arguments are provided, a new figure is opened.
- If a fourth argument is provided, the function either uses the current
figure or opens a new one based on the `holdon` flag.
- For each planet, compute and plot its orbit over the specified time range.
- The orbits are plotted in Astronomical Units (AU) with the Sun's position
marked as a yellow point.

## Function Signature
```matlab
[fig] = plotPLTS_tt(pl, t0, tend, idcentral, customEphemerides, holdon, colors, names, linewidth, style)
```
