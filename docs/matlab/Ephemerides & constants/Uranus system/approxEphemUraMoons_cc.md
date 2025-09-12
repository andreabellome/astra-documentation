# `approxEphemUraMoons_cc`

## INPUTS
- idmoon: number indicating which Uranus moon to consider.
- t: Epoch at which moon state vector & Orbital Elements are to be
computed, expressed in days past since MJD2000.
OUTPUTS %%
- rr: Moon position vector components  at the desired epoch in [km].
- vv: Moon velocity vector components at the desired epoch in [km/s].
- kep: 1x6 vector of orbital elements ordered as [a, e, i, Om, om, th],
where th is the true anomaly. Angles in [rad], semi-major axis in [km].
CHANGELOG %%
27/08/2024, J.C Garcia Mateas: corrected the Orbital Elements for the
reference epoch & added function description & comments.
FUNCTIONS %%

## Function Signature
```matlab
[rr, vv, kep] = approxEphemUraMoons_cc(idmoon, t)
```
