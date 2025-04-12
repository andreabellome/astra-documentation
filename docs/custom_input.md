This tutorial shows how to include some custom input parameters to ASTRA optimization. These are the following:

- Custom boundaries for time of flight between planets
- Custom maximum overall mission duration
- Custom boundaries of infinity velocities $ v_{\infty} $ at different bodies encounters
- Custom ephemerides
- Custom objective functions for both SODP and MODP

## Customising boundaries

This section shows how to add custom boundaries to time of flight, overall mission duration, and infinity velocities at objects' encounters.

This is very easy to do in ASTRA as one needs to select the following optional input to be appended to the ```INPUT``` structure:

```matlab
seq = [ 3 2 3 3 5 ]; res = [ 2 1 3 ];

INPUT.TOF_LIM = [ 100 500; 100 500; 100 500; 500 2000 ]; % --> min./max TOF [days] for each leg
INPUT.vInfLim = [ 0 5; 0 9; 0 11; 0 11; 0 7 ];           % --> min./max infinity velocity [km/s] for each planet 
```

- The field ```INPUT.TOF_LIM``` specifies the minimum and maximum time of flight for each leg -- a leg is a planet-to-planet transfer. Thus, in the example, one has 5 planets (EVEEJ) and 4 legs (EV, VE, EE, EJ). One notices that a resonance is specified on the 3rd leg. Therefore, setting up the time-of-flight bounds on that leg **it has no effect** (the resonance dictates the time).

- Similarly, the field ```INPUT.vInfLim``` specifies minimum and maximum infinity velocities at planetary encounters. One should specify one for each planet. If the target object is a comet/asteroid, then the bounds on infinity velocity actually correspond to the bounds for a $ \Delta v $ to rendezvous with the object.

- Finally, the field ```INPUT.tofy``` allows to set-up the maximum transfer time **in years** of the whole trip.




## Custom ephemerides



## Custom objective funcrtions