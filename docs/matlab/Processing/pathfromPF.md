# `pathfromPF`

## DESCRIPTION
This function extracts a specific path and the associated parameters
from the Pareto Front (PF) results. If no specific row is provided, it
retrieves the best path based on the minimum cost.

## INPUT
- OUTPUT : Struct array containing results from multiple runs, including
details like paths, revolutions, and costs.
- outNumber : row ID of the OUTPUT structure.
- rowPF  : Optional index specifying the row of the Pareto Front to extract.
If not provided, the function selects the best path based on cost.
- customEphemerides : user-defined custom ephemerides. See
EphSS_cartesian.m for reference.

## OUTPUT
- path   : Matrix representing the trajectory path extracted from the specified
Pareto Front row or the best path if no row is specified.
- revs   : Array of revolutions corresponding to the specified Pareto Front row
or the best path if no row is specified.
- res    : Resolution used for the trajectory computation, either from the
specified Pareto Front row or the best path if no row is specified.

