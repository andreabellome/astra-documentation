# `wrapSolveFopt`

## DESCRIPTION
This function solves the fuel-optimal low-thrust problem.

## INPUT:
- param: structure with the required parameters from
processDataAndWriteParam.m

## OUTPUT:
- LTsol: structure with the following fields:
- transfer : Matrix containing the processed trajectory data with the
following columns:
[time (days), position (km), velocity (km/s), mass (kg),
thrust magnitude (N), thrust vector (N)].
- lambdas: initial conditions for the co-states for
fuel-optimal problem
- Tmax    : max. thrust [N]
- Isp     : specific impulse [s]
- g0      : gravitational acceleration at sea level [m/s2]
- m0      : initial mass [kg]
- mf      : final mass [kg]
- tof     : time of flight [days]
- DV      : DV of the low-thrust transfer [km/s]
- param   : structure with relevant parameters for the solution
- success : boolean to check if the solver has succeeded or not

## Function Signature
```matlab
[LTsol] = wrapSolveFopt( param )
```
