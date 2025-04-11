This page shows how to integrate NASA high-precision ephemerides in ASTRA. This is particularly useful when using different planetary systems or when trips to comets or asteroids are sought.

## Integrating NASA ephemerides for Solar System planets

Before considering other bodies, let's consider the Solar System planets. As from the [intallation guide](./install.md), one should have the following structure in the local directory:

```pgsql
local-folder/
├── ASTRA
├── MICE_TOOLBOX/
    ├── mice/
        ├── Kernel/
            ├── de430.bsp
            ├── gm_de431.tpc
            ├── mar097.bsp
            ├── naif0012.tls
            ├── pck00010.tpc
            └── sat375.bsp
        ├──mice
├── clearDeleteAdd.m
└── main_script.m
```

The ```main_script.m``` is the one we want to modify (see, for example the tutorial on [trips to Jupiter](./trips_to_jupiter.md) or <a href="https://github.com/andreabellome/astra/blob/main/astra_with_custom_eph_mice.m" target="_blank">this script</a>).

After having set-up all the input and the ASTRA environment, one needs to load the NASA ephemerides. This can be done by imposing that:

```matlab
% --> load MICE toolbox
MICE_path = './MICE_TOOLBOX' ;
addpath(genpath(MICE_path)); % --> always include this
cspice_furnsh([MICE_path '/data.mk']);
```

In this way, one loads the kernels for planetary ephemerides. This is not sufficient. One needs to tell ASTRA which ephemerides it should use. The default ones are encoded in the script <a href="https://github.com/andreabellome/astra/blob/main/ASTRA/Ephemerides%20%26%20constants/Solar%20System/EphSS_cartesian.m" target="_blank">EphSS_cartesian.m</a>. To overwrite those, one can simply set:

```matlab
INPUT.customEphemerides = @EphSS_from_mice;
```

In particular, the function <a href="https://github.com/andreabellome/astra/blob/main/ASTRA/Ephemerides%20%26%20constants/Eph_MICE_interface/EphSS_from_mice.m" target="_blank">EphSS_from_mice.m</a> allows to automatically use the NASA ephemerides.

That's it. 

Then one can launch an optimization for the EVEMEJ similar to the tutorial on [trips to Jupiter](./trips_to_jupiter.md). Obviously, the two optimizations should provide very similar result:

- the one with **approximate ephemerides** has a minimum cost of: **8.94774 km/s** and **6.45038 years**
- the one with **NASA ephemerides** has a minimum cost of: **8.95409 km/s**  and **6.45038 years**

which indeed are very close. Thus, if one needs to plan missions to any of the solar system planet, the approximate ephemerides are suggested, as these are quite faster to compute with respect to high-precision ones.

**BUG DETECTED: currently, high-precision NASA ephemerides prevent ASTRA to be run in parallel mode when resonances are present in the sequence. A work-around to this is shown later, but a rearchitect is needed. This will be solved in the next update...**

## Integrating NASA ephemerides for small objects

A very interesting application for integrating NASA ephemerides into ASTRA is when one needs to plan missions to Solar System objects that are not planets (asteroids and/or comets). This opens a very wide range of possibilities in terms of mission design.
