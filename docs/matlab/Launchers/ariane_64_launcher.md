# `ariane_64_launcher`

## DESCRIPTION:
Launch mass from infinity-velocity for Ariane 64 launcher.
This function supports both mono-boost and bi-boost launcher
configurations.
IMPORTANT: if the dla_deg is outside -5/+5 deg bounds, the function
automatically selects the bi-boost configuration to maximise the mass.

## INPUT:
- vinf         : infinity velocity at launch [km/s]
- dla_deg      : launch declination [deg]. Default is -5 deg (max.
performance of the launcher)
- mass_adapter : adapter mass [kg]. By default = 110 kg
- type         : string. Launcher type either 'mono_boost' or 'bi_boost'.
By default is 'mono_boost'. However, if the launch
declination is either more than 5 deg or less than -5
deg, then the performances of the mono-boost are too low
and thus the 'bi_boost' option is automatically
selected.

## OUTPUT:
- m0 : max. launch mass [kg]

## Function Signature
```matlab
[m0] = ariane_64_launcher( vinf, dla_deg, mass_adapter, type )
```
