# `wrapSolveFoptSEP`

## DESCRIPTION
This function solves the fuel-optimal low-thrust problem
using Solar Electric Propulsion (SEP). The thrust profile can be seen in
the function func_thrust_fitted.m

## INPUT:
- param: structure with the required parameters from
processDataAndWriteParam.m
additional REQUIRED parameters are:
- n_engines     : number of engines
- thrust_max_N  : reference thrust for each engine [N] (e.g.,
0.255 N)
- epsilon       : smooth factor for the thrust profile (by
default 0.002)
- initial_guess : initial guess on the co-states (by default, a
random guess is provided). It is STRONGLY RECOMMENDED to solve
first a LT problem with max. thrust using wrapSolveFopt.m and
then to use that solution as initial guess for the SEP problem.

## OUTPUT:
- LTsol: structure with the following fields:
- transfer : Matrix containing the processed trajectory data with the
following columns:
[time (days), position (km), velocity (km/s), mass (kg),
thrust magnitude (N), thrust vector (N)].
- lambdas: initial conditions for the co-states for
fuel-optimal problem using SEP
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
[LTsol] = wrapSolveFoptSEP( param )
```
