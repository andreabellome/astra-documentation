# `paretoFront_MODP`

## DESCRIPTION
Wrapper for computing Pareto front in MODP.

## INPUT
- COSTmatrix : N-by-D matrix, where N is the number of points and D is the
number of elements (objectives) of each point.

## OUTPUT
- PARETO_FRONT : matrix with Pareto front as follows:
- PARETO_FRONT(:,1:N) : objectives on the front
- PARETO_FRONT(:,end) : rows' IDs of the point in
COSTmatrix
- PARETO_UNIQUE : same as PARETO_FRONT but with unique points w.r.t. the
first objective

## Function Signature
```matlab
[PARETO_FRONT, PARETO_UNIQUE] = paretoFront_MODP( COSTmatrix )
```
