# `check_INPUT`

## INPUT
- vInfLim        : (Optional) Vector defining the range of departure infinity velocities (km/s).
If not provided, defaults to an empty array.
- TOF_LIM        : (Optional) Vector defining the range of times of flight (days).
If not provided, defaults to an empty array.
- tstep          : (Optional) Scalar specifying the discretization time step (days).
If not provided, defaults to 2 days.
- tofyMax        : (Optional) Scalar defining the maximum time of flight (days).
If not provided, defaults to an empty array.
- costFunc1      : (Optional) Function handle for the first cost function in single-objective optimization.
If not provided, defaults to `costFunction1_DP`.
- costFunc2      : (Optional) Function handle for the second cost function in single-objective optimization.
If not provided, defaults to `costFunction2_DP`.
- costFunc1_BS   : (Optional) Function handle for the first cost function with a specific approach.
If not provided, defaults to `costFunction1_BS`.
- costFunc2_BS   : (Optional) Function handle for the second cost function with a specific approach.
If not provided, defaults to `costFunction2_BS`.
- costFunc1_MODP : (Optional) Function handle for the first cost function in multi-objective optimization.
If not provided, defaults to `costFunction1_MODP`.
- costFunc2_MODP : (Optional) Function handle for the second cost function in multi-objective optimization.
If not provided, defaults to `costFunction2_MODP`.
OUTPUT:
vinflim           : Extracted or default value for the vInfLim field.
TOF_LIM           : Extracted or default value for the TOF_LIM field.
tstep             : Extracted or default value for the tstep field.
tofyMax           : Extracted or default value for the tofyMax field.
costFunc1         : Extracted or default function handle for costFunc1.
costFunc2         : Extracted or default function handle for costFunc2.
costFunc1_BS      : Extracted or default function handle for costFunc1_BS.
costFunc2_BS      : Extracted or default function handle for costFunc2_BS.
costFunc1_MODP    : Extracted or default function handle for costFunc1_MODP.
costFunc2_MODP    : Extracted or default function handle for costFunc2_MODP.

