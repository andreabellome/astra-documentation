# `processDataAndWriteParam`

## INPUT:
m0          : initial mass                                        [kg]
tof         : time of flight                                      [s]
state1      : initial state                                       [km],[km/s]
state2      : final state                                         [km],[km/s]
Tmax        : max. thrust                                         [N]
Isp         : specific impulse                                    [s]
g0          : Earth acceleration at sea level (default: 9.80665)  [m/s2]
Nrev        : number of revolutions (default: 0)
idcentral   : ID of the central body (default: 1, i.e., Sun)
useParallel : if true, uses parallel for fsolve (default: false)

## OUTPUT:
param : structure with all the info needed for running the solver

## Function Signature
```matlab
[param] = processDataAndWriteParam(m0, tof, state1, state2, Tmax, Isp, g0, Nrev, idcentral, useParallel)
```
