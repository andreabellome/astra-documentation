# `writeParamLT`

## DESCRIPTION
This function initializes and returns a parameter structure required for
low-thrust trajectory optimization. The structure contains constants,
scaled parameters, and solver options used in the optimization process.

## INPUT
- Tmax       : Maximum thrust (N).
- Isp        : Specific impulse (s).
- m0         : Initial mass (kg).
- g0         : Standard gravitational acceleration (m/s^2). Default is 9.8065.
- idcentral  : ID of the central body (1 for Sun, other planets correspond
to their respective IDs). Default is 1.
- useParallel: Boolean to specify if parallel computation should be used.
Default is false.

## OUTPUT
- param : Structure containing the following fields:
- mu          : Gravitational parameter of the central body (km^3/s^2).
- AU          : Astronomical unit (km).
- Tmax        : Maximum thrust (N).
- g0          : Gravitational acceleration (m/s^2).
- Isp         : Specific impulse (s).
- day         : Duration of one day (s).
- year        : Duration of one year (days).
- useEdelbaum: Boolean for using Edelbaum approximation (default false).
- LU          : Length unit (km).
- TU          : Time unit (s).
- MU          : Mass unit (kg).
- muScl       : Scaled gravitational parameter.
- IspScl      : Scaled specific impulse.
- TmaxScl     : Scaled thrust.
- g0Scl       : Scaled gravitational acceleration.
- m0Scl       : Scaled initial mass.
- fsolveoptions: Options for the fsolve function, including tolerances,
maximum evaluations, and parallel computation settings.
- odeoptions  : Options for ODE solvers, including tolerances.
- bvpoptions  : Options for boundary value problem solvers, including
tolerances and statistics.
- plots       : Boolean for enabling/disabling plots (default false).
- full        : Boolean for enabling/disabling full output (default false).

## Function Signature
```matlab
[param] = writeParamLT( Tmax, Isp, m0, g0, idcentral, useParallel)
```
