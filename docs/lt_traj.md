This tutorial shows how to solve **fuel-optimal time-fixed optimal control problem** on each leg of the MGA trajectory under consideration. With the current functions available in ASTRA, also the **time-fixed energy-optimal control problem** is solvable, but not direct function is available via user-friendly API.

*It has to be said that to solve the fuel-optimal time-fixed optimal control problem ASTRA uses the solution from the time-fixed energy-optimal control problem as initial guess*.

Two representative test cases are shown:

- An Earth-Mars transfer, realtively easy to solve as less than 1 revolution is needed to perform the transfer. Plus, the planets have very similar inclinations.

- A transfer from Earth to Dionysus asteroid, where multiple revolutions are needed and the inclination change substantially (approx. 13 degrees).

One can find the reference script for these tutorials at [this link](https://github.com/andreabellome/astra/blob/main/low_thrust_trajectories.m).

## Earth-Mars

The first test case is an Earth-Mars transfer.

One should select the system parameters:

```matlab
clearDeleteAdd; % --> !!! ONLY CALL IT ONCE FOR SPEED

% --> parameters
idcentral   = 1;          % --> 1) central body is the Sun
Tmax        = 0.5;        % --> max. thrust                       [N]
Isp         = 2000;       % --> specific impulse                  [s]
m0          = 1000;       % --> initial mass                      [kg]           
g0          = 9.80665;    % --> Earth acceleration at sea level   [m/s]
useParallel = false;      % --> if true, uses parallel for fsolve
```matlab

Then one specifies the time of flight (in seconds), initial and final states (in km and km/s, for position and velocity, respectively), as well as the desired number of revolutions:

```matlab
tof    = 348.795 * 86400;                                                       % --> time of flight [sec]
state1 = [ -140699693 -51614428 980 9.774596  -28.07828  4.337725e-4 ];         % --> initial state [km],[km/s]
state2 = [ -172682023 176959469 7948912 -16.427384  -14.860506  9.21486e-4 ];   % --> final state [km],[km/s]
Nrev   = 0;                                                                     % --> number of revolutions
```

A function is called to process such parameters:

```matlab
% --> initialise the parameters
param = processDataAndWriteParam(m0, tof, state1, state2, Tmax, Isp, g0, Nrev, idcentral, useParallel);
```

The user can then modify some of them to meet the desired accuracy:

```matlab
% --> you might want to overwrite some of those (some examples below)
param.rhoLim                                = 0.0001;
param.rho                                   = 1;
param.gamma                                 = 0.1;
param.plot                                  = true;    % --> this plots the thrust evolution over time for different rho (default is false)
param.fsolveoptions.MaxFunctionEvaluations  = 10e3;
param.fsolveoptions.MaxIterations           = 10e3;
```

Specifically, ```rhoLim```, ```rho``` and ```gamma``` are smoothing parameters that help solving the fuel-optimal problem. Having in mind that the fuel-optimal problem has a bang-off-bang optimal control, one has as general rules that:

- ```rho``` dictates the transition from energy-optimal to fuel-optimal problem. A low value (e.g., ```0.0001```) will make the transition quite steep, and the fuel-optimal problem might not converge. A high value (max. is 1) will allow a smoother transition, but it will take more time to converge. Suggested values are ```0.75``` to ```1```.

- ```rhoLim``` dictates the quality of the fuel-optimal solution. A small value (e.g., ```0.0001```) will make the smooth problem to be basically identical to a pure fuel-optimal problem, but it will take more time to run. Higher values correspond to smooth final solutions, not precisely corresponding to optimal trajectories. Values between ```0.0001``` and ```0.01``` are suggested.

- ```gamma``` is the factor that cuts progressively ```rho```, solving smoother problems at each iteration. A high value (max. is ```1```) makes the transition from smooth problems to non-smooth quite gentle, helping the convergence, but sacrifycing the computing time. A small value makes the transition quite steep, saving computing time but potentially reducing convergence. Suggested values are ```0.1``` (simple problems) to ```0.95``` (complex problems).

Finally, one can solve the problem:

```matlab
% --> solve the problem
LTsol = wrapSolveFopt( param );
```

The solution is contained in the ```LTsol.transfer``` variable, which is used to plot the results:

```matlab
% --> plot the solution
transfer = LTsol.transfer;
[figTRAJ, figMASS, figTHRmag] = plotLT( transfer, param );

% --> add Mars and Earth orbits to the plot
figure(figTRAJ);
plotPLTS_tt([3 4], 0, 3*365.25, idcentral, @EphSS_cartesian, 1);
```

**INCLUDE IMAGES HERE**

## Earth-Dionysus

As before, the system parameters are defined. In this case, one gives the states directly in Mean Equinoctial Elements (MEE), so a different function is used to build the parameters:

```matlab
% --> parameters
idcentral = 1;        % --> 1) central body is the Sun
Tmax      = 0.32;     % --> max. thrust                       [N]
Isp       = 3000;     % --> specific impulse                  [s]
m0        = 4000;     % --> initial mass                      [kg]          
g0        = 9.80665;  % --> Earth acceleration at sea level   [m/s]

% --> initialise the parameters
param     = writeParamLT( Tmax, Isp, m0, g0, idcentral, true );
```

Then, one manually builds the initial and final states. Note that in this case, the optimal solution corresponds to ```Nrev = 5```:

```matlab
% --> Earth-to-Dionysus
tStart    = 0;
tEnd      = 3534; % --> please note that in this case the tof is in [days] as this is already scaled!!!
initState = [ 0.999316, -0.004023, 0.015873, -1.623e-5, 1.667e-5, 1.59491 ];
finState  = [ 1.555261 0.152514 -0.519189 0.016353 0.117461 2.36696 ];

param.tStart = tStart;
param.tEnd   = tEnd;
param.x0     = initState;
param.xf     = finState;

param.rhoGuess1 = 0.75;
param.plot      = true;
param.rhoLim    = 0.0001;
param.rho       = 1;
param.gamma     = 0.1;
param.iterMax   = 5;
param.tol       = 1e-8;

while param.xf(end) < param.x0(end)
    param.xf(end) = param.xf(end) + 2*pi;
end

Nrev            = 5;
param.xf(end)   = param.xf(end) + 2*Nrev*pi;
```

As before, one can solve the problem by calling:

```matlab
% --> solve the problem
LTsol = wrapSolveFopt( param );
```

The solution is plotted:

```matlab
% --> plot the solution
transfer                      = LTsol.transfer;
[figTRAJ, figMASS, figTHRmag] = plotLT( transfer, param );

figure(figTRAJ);
view( [-19 13] );
plotPLTS_tt(3, 0, 2*365.25, idcentral, @EphSS_cartesian, 1); % --> add Earth orbit to the plot
```

**INCLUDE IMAGES HERE**



