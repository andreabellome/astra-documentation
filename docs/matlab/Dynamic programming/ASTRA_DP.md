# `ASTRA_DP`

## DESCRIPTION
This is a wrapper for all ASTRA functionalities.

## INPUT
- seq      : vector with planets IDs in the MGA sequence
- INPUT    : structure with the following mandatory fields:
- chosenRevs :
- res        : vector with N:M resonant ratio and number
of leg at which the resonant transfer is needed. If no
resonant transfer is needed, leave it empty. E.g. EVEMMMJ
with 2:1 and 3:1 on MM legs would have:
res = [ 2 1 4 3 1 5 ], where 4 and 5 are the legs in which
the 2:1 and 3:1 occurr.
- depOpts    : 1x2 vector. depOpts(1) is for initial date
range (MJD2000), depOpts(2) is for final date range
(MJD2000), and depOpts(3) is for step size (days)
- opt        : (1) is for SODP, (2) is for MODP, (3) is
for DATES, (4) is for YEARS - MODP
- vInfOpts   : min/max departing infinity velocities (km/s)
- dsmOpts    : max defect DSM (km/s), and total DSMs (km/s)
- plot       : 1x2 vector. plot(1) is for plotting the
best DV trajectory, plot(2) is for plotting the Pareto
front. Please put plot(i)=1 if you want to plot the results.
- parallel   : if 1, then parallel computing is used
- tstep      : (days) discretization time step

## OUTPUT
- OUTPUT : structure with the final trajectories

## Function Signature
```matlab
[OUTPUT] = ASTRA_DP(seq, INPUT)
```
