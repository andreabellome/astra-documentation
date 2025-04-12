This tutorial shows how to include some custom input parameters to ASTRA optimization. These are the following:

- Custom boundaries for time of flight between planets
- Custom maximum overall mission duration
- Custom boundaries of infinity velocities $ v_{\infty} $ at different bodies encounters
- Custom ephemerides
- Custom objective functions for both SODP and MODP

## Custom boundaries

This section shows how to add custom boundaries to time of flight, overall mission duration, and infinity velocities at objects' encounters.

This is very easy to do in ASTRA as one needs to select the following optional input to be appended to the ```INPUT``` structure:

```matlab
% --> sequence and resonances
seq = [ 3 2 3 3 5 ]; res = [ 2 1 3 ];

%%%%%%%%%% multi-rev. options %%%%%%%%%%
maxrev                        = 1;                                                          % --> max. number of revolutions (round number)
chosenRevs                    = differentRuns_v2(seq, maxrev);                              % --> generate successive runs
[INPUT.chosenRevs, INPUT.res] = processResonances(chosenRevs, res);                         % --> process the resonances options
[INPUT.chosenRevs]            = maxRevOuterPlanets(seq, INPUT.chosenRevs, INPUT.idcentral); % --> only zero revs. on outer planets
%%%%%%%%%% multi-rev. options %%%%%%%%%%

%%%%%%%%%% set departing options %%%%%%%%%%
t0 = date2mjd2000([2023 1 1 12 0 0]); % --> initial date range (MJD2000)
tf = t0 + 1*365.25;                   % --> final date range (MJD2000)
dt = 5;                               % --> step size (days)
INPUT.depOpts = [t0 tf dt];
%%%%%%%%%% set departing options %%%%%%%%%%

%%%%%%%%%% set options %%%%%%%%%%
INPUT.opt      = 1;          % --> (1) is for SODP, (2) is for MODP, (3) is for DATES - SODP, (4) is for YEARS - MODP
INPUT.vInfOpts = [0 4];      % --> min/max departing infinity velocities (km/s)
INPUT.dsmOpts  = [1 Inf];    % --> max defect DSM, and total DSMs (km/s)
INPUT.plot     = [1 1];      % --> plot(1) for Pareto front, plot(2) for best traj. DV
INPUT.parallel = true;       % --> put true for parallel, false otherwise
INPUT.tstep    = 3;          % --> step size for Time of flight            
%%%%%%%%%% set options %%%%%%%%%%

%%%%%%%%%% custom boundaries %%%%%%%%%%
INPUT.TOF_LIM = [ 100 500; 100 500; 100 500; 500 2000 ]; % --> min./max TOF [days] for each leg
INPUT.vInfLim = [ 0 5; 0 9; 0 11; 0 11; 0 7 ];           % --> min./max infinity velocity [km/s] for each planet 
INPUT.tofyMax = 7;                                       % --> max. overall mission duration [years]
%%%%%%%%%% custom boundaries %%%%%%%%%%
```

Specifically:

- The field ```INPUT.TOF_LIM``` specifies the minimum and maximum time of flight for each leg -- a leg is a planet-to-planet transfer. Thus, in the example, one has 5 planets (EVEEJ) and 4 legs (EV, VE, EE, EJ). One notices that a resonance is specified on the 3rd leg. Therefore, setting up the time-of-flight bounds on that leg **it has no effect** (the resonance dictates the time).

- Similarly, the field ```INPUT.vInfLim``` specifies minimum and maximum infinity velocities at planetary encounters. One should specify one for each planet. If the target object is a comet/asteroid, then the bounds on infinity velocity actually correspond to the bounds for a $ \Delta v $ to rendezvous with the object. One should notice that infinity velocity bounds at the first planet are not effective as one should **always** specify:

    ```matlab
    INPUT.vInfOpts = [0 5];      % --> min/max departing infinity velocities (km/s)
    ```

    Obviously, if the first object of the sequence is an asteroid/comet, this is equivalent to a $ \Delta v $ to depart from it.

- Finally, the field ```INPUT.tofyMax``` allows to set-up the maximum transfer time **in years** of the whole trip.

## Custom ephemerides

Customising ephemerides function requires a bit of coding.

Essentially, ASTRA works with approximate planetary positions encoded in the script <a href="https://github.com/andreabellome/astra/blob/main/ASTRA/Ephemerides%20%26%20constants/Solar%20System/EphSS_cartesian.m" target="_blank">EphSS_cartesian.m</a>. These are proven to be sufficiently close to NASA high-precsion ones (e.g., <a href="https://naif.jpl.nasa.gov/pub/naif/generic_kernels/spk/planets/" target="_blank">de430.bsp</a>), as shown in [this tutorial](./nasa_ephemerides.md).

If one wants to specify a custom function (say ```Eph_custom```), the template should be:

```matlab
function [ rr, vv ] = Eph_custom( pl, t, idcentral )

% --> here the logic...

end
```

Where in input is required:

- ```pl``` is the ID of the body
- ```t``` is the epoch at which the ephemerides are computed in **MJD2000**
- ```idcentral``` should specify the central body (e.g., ```idcentral=1``` if the Sun is the central body)

The output are:

- ```rr```: a ```3x1``` vector with object position in consistent reference frame, expressed in **km**
- ```vv```: a ```3x1``` vector with object velocity in consistent reference frame, expressed in **km/s**

Finally, in the main script one simply sets the following before launching the optimization:

```matlab
idcentral               = 1;                                        % --> specify the central body
INPUT.customEphemerides = @( pl,t ) Eph_custom( pl, t, idcentral ); % --> specify the custom ephemerides function
```

In this way, ASTRA uses the custom ephemerides function defined by the user. 

## Custom objective functions

Customising objective functions requires a bit of coding. 

