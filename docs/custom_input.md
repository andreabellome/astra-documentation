This tutorial shows how to include some custom input parameters to ASTRA optimization. These are the following:

- Custom boundaries for time of flight between planets
- Custom maximum overall mission duration
- Custom boundaries of infinity velocities $ v_{\infty} $ at different bodies encounters
- Custom objective functions for both SODP and MODP

## Customising boundaries

This section shows how to add custom boundaries to time of flight, overall mission duration, and infinity velocities at objects' encounters.

This is very easy to do in ASTRA as one needs to select the following optional input to be appended to the ```INPUT``` structure:

