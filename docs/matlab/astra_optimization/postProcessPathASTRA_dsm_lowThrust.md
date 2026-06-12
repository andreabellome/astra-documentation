# `postProcessPathASTRA_dsm_lowThrust`

## DESCRIPTION
THIS FUNCTION IS STILL WORK IN PROGRESS!!
This function processes the output of a low-thrust trajectory optimization
problem to generate a structured output. It calculates velocity adjustments
(DSM), ephemerides, and departure/arrival states, while considering constraints
such as flyby conditions and central body parameters.

## INPUT
- dv        : list of impulsive DVs along the MGA as from the function
wrap_mga_nDSM.m
- output    : structure of the MGA trajectory with DSMs as from the
function wrap_mga_nDSM.m
- MAT       : matrix with details of the MGA trajectory as from the
function wrap_mga_nDSM.m
- vdep_free : departure infinity velocity provided by the launcher 'for
free' - if 0, then a departure manoeuvre is imparted by the
SC [km/s]
- varr_free : scalar, maximum arrival velocity (default is 0 if not
provided) [km/s] - if 0, a rendezvous with the final object
is assumed.
- idcentral : scalar, central body identifier (default is 1 for Sun) -
see also constants.m
- customEphemerides : anonymous function defining the custom ephemerides.
- decl_min  : min. declination angle at launch [rad] (by dafault -Inf)
- decl_max  : max. declination angle at launch [rad] (by dafault +Inf)

## OUTPUT
- struc : structure containing detailed information about the trajectory,
including departure and arrival states, velocity adjustments,
and ephemerides for each transfer leg.

