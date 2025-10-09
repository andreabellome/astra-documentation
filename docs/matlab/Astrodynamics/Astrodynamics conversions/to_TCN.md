# `to_TCN`

## DESCRIPTION
This function rotates a vector from an inertial reference frame
to the local orbital frame defined as Tangential–Cross-track–Radial-like
(TCN). The transformation is based on the instantaneous position and
velocity vectors of the spacecraft.

## INPUT
- r   : position vector [3x1] or [1x3] in the inertial reference frame [km]
- v   : velocity vector [3x1] or [1x3] in the inertial reference frame [km/s]
- vec : vector [3x1] or [1x3] to rotate in the inertial reference frame

## OUTPUT
- dv_tcn : delta-v components in the TCN frame [1x3] = [dv_T, dv_C, dv_N],
where:
- dv_T = component along the tangential direction (velocity)
- dv_C = component along the cross-track direction (orbital angular momentum)
- dv_N = component along the radial-like direction (toward position vector)

## Function Signature
```matlab
[dv_tcn] = to_TCN(r, v, vec)
```
