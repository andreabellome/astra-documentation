# `costFunction2_MODP_vdep_varr`

## DESCRIPTION
This function evaluates multiple trajectory options and selects those on the Pareto front,
considering both delta-v and time-of-flight. It also identifies the minimum delta-v trajectory.

## INPUT
- legn  : matrix containing trajectory leg parameters, where columns represent
different trajectory characteristics such as departure time, arrival
time, and delta-v components.
- vvf   : matrix containing final velocity vectors for each trajectory leg.
- vinff : matrix containing incoming hyperbolic excess velocities.
- vdep  : scalar value representing the specified departure velocity.
- varr  : scalar value representing the specified arrival velocity.
- sigma : weighting factor for the time-of-flight in the total cost computation.

## OUTPUT
- legn     : matrix containing the trajectory legs that belong to the Pareto front.
- vvf      : matrix containing the final velocities of the Pareto-optimal trajectories.
- vinff    : matrix containing the incoming excess velocities of the Pareto-optimal trajectories.
- PF       : matrix representing the Pareto front, storing time-of-flight and total cost.
- COSTS    : vector containing the total cost (delta-v + weighted time-of-flight) for each trajectory.
- TOFYS    : vector containing the time-of-flight values in years.
- minCOST  : scalar value of the minimum total cost among all solutions.
- row      : index of the trajectory corresponding to the minimum total cost.

## PROCESS
1. Compute the departure delta-v (dv1) and arrival delta-v (dv2), ensuring non-negative values.
2. Compute the total time-of-flight (tofs).
3. Compute the total delta-v (dvtot) including all intermediate maneuvers.
4. Compute the cost for each trajectory as the sum of delta-v and weighted time-of-flight.
5. Construct the cost matrix containing time-of-flight and total cost.
6. Compute the Pareto front from the cost matrix.
7. Select the trajectories that belong to the Pareto front.
8. Identify and return the minimum delta-v trajectory.

## Function Signature
```matlab
[legn, vvf, vinff, PF, COSTS, TOFYS, minCOST, row] = costFunction2_MODP_vdep_varr(legn, vvf, vinff, vdep, varr, sigma)
```
