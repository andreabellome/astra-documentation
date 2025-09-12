# `process_paretoFront_structure`

## DESCRIPTION
This function processes the output of a multi-objective trajectory
optimization routine for multiple gravity assist trajectories by
converting the raw results into a user-friendly structured format. It
extracts and organizes path details, objective values, times of flight,
and dynamical defects for each point on the Pareto front.

## INPUT
- INPUT            : structure containing mission setup parameters,
including the objective functions and SPICE settings
- processed_OUTPUT : structure containing raw optimization results,
including legs, velocities, and revolution data

## OUTPUT
- paretoFront : structured array where each element contains the
following fields for a single trajectory on the Pareto front:
* path        : full trajectory path as time-state matrix
* revs        : sequence of revolutions for each leg
* res         : additional resolution data
* objVal      : values of the objective functions
* tof_days    : total time of flight in days
* tof_years   : total time of flight in years
* tofs_days   : vector of times of flight for each leg (days)
* vinfDep     : launch hyperbolic excess velocity (km/s)
* vinfArr     : arrival hyperbolic excess velocity (km/s)
* defects     : vector of dynamical defects per leg
* defects_sum : sum of all dynamical defects

## Function Signature
```matlab
[ paretoFront ] = process_paretoFront_structure( INPUT, processed_OUTPUT )
```
