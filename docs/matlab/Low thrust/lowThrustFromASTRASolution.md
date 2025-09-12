# `lowThrustFromASTRASolution`

## DESCRIPTION
This function is used to process the ASTRA solution for low-thrust trajectory optimization.
It processes the trajectory data, computes the thrust profile, and solves for the optimal
solution based on the given parameters and constraints. If the thrust system is insufficient
for any leg of the trajectory, it terminates early. It generates an output structure that includes
the trajectory details, including mass evolution, delta-v, and time of flight for each leg of the mission.

## INPUT
- astraSolution : structure containing ASTRA solution data
- path      : trajectory path data
- revs      : revolutions' options for each leg
- res       : resonance options for each leg
- vdep_free : velocity for free departure [km/s]
- varr_free : velocity for free arrival [km/s]
- lowThrustParameters : structure containing low-thrust trajectory parameters
- Tmax          : maximum thrust [N]
- Isp           : specific impulse [s]
- m0            : initial mass [kg]
- gamma         : discount factor for the smoothing parameter (default is 0.5)
- rhoLim        : limit on the smoothing parameter for optimal control solution (default is 0.001)
- plot          : boolean flag to enable plotting of the thrust profile (default is false)
- useParallel   : boolean flag to enable parallel computation (default is false)
- g0            : gravitational acceleration constant [m/s^2]
- idcentral         : ID of the central body for the transfer
- customEphemerides : function handle for custom ephemerides

## OUTPUT
- LT_SOLUTION : structure containing the low-thrust trajectory solution
- LTsol : low-thrust solution for each leg, including mass, time of flight,
delta-v, and other trajectory details
- m0                : initial mass at the beginning of the leg
- mf                : final mass after the leg
- mp                : mass change during the leg
- DV                : delta-v for the leg
- tof               : time of flight for the leg
- cumulative_tof    : cumulative time of flight for all legs

## Function Signature
```matlab
[LT_SOLUTION, struc] = lowThrustFromASTRASolution( astraSolution, lowThrustParameters, idcentral, customEphemerides )
```
