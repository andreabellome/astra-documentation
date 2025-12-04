# `ariane_62_launcher`

## DESCRIPTION:
1D exponential function with 4th degree polynominal to get the launch
mass from infinity-velocity for Ariane 62 launcher (no info on
declination)

## INPUT:
- vinf         : infinity velocity at launch [km/s]
- mass_adapter : adapter mass [kg]. By default = 110 kg

## OUTPUT:
- m0 : max. launch mass [kg]

## Function Signature
```matlab
[m0] = ariane_62_launcher( vinf, mass_adapter )
```
