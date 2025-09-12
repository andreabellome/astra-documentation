# `plotLT`

## DESCRIPTION
This function plots the trajectory, mass evolution, and thrust magnitude
for a low-thrust space trajectory. Depending on the number of requested

## INPUT
- transfer: Matrix containing trajectory and associated parameters:
Column 1  : Time [days]
Columns 2-4: Position (x, y, z) [km]
Columns 5-7: Velocity (vx, vy, vz) [km/s]
Column 8  : Spacecraft mass [kg]
Column 9  : Thrust magnitude [N]
- param: Structure containing simulation parameters:
- param.AU: Astronomical Unit [m], used to scale positions to AU

## OUTPUT
- Trajectory in 3D space
- Mass evolution over time
- Thrust magnitude over time
- figTRAJ   : Figure handle for the trajectory plot
- figMASS   : Figure handle for the mass evolution plot (optional)
- figTHRmag : Figure handle for the thrust magnitude plot (optional)

## Function Signature
```matlab
[figTRAJ, figMASS, figTHRmag] = plotLT( transfer, param, holdon )
```
