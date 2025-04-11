# Installation

CIAOOO 

## Requirements

To run a full exploration of MGA trajectories, the following system requirements are recommended:

+ CPU six-core from 2.6 GHz to 3.6 GHz.
+ RAM minimum 16 GB.
+ Any version of <a href="https://it.mathworks.com/products/matlab.html" target="_blank">MATLAB</a> ≥2021b.
+ A compiler for C functions should be used. You can use the <a href="https://it.mathworks.com/matlabcentral/fileexchange/52848-matlab-support-for-mingw-w64-c-c-fortran-compiler" target="_blank">minGW</a>.
+ (*optional*) <a href="https://it.mathworks.com/products/parallel-computing.html" target="_blank">MATLAB Parallel Computing Toolbox</a>. This is needed to run ASTRA in parallel mode, and to use the low-thrust module.
+ (*optional*) <a href="https://it.mathworks.com/products/optimization.html" target="_blank">MATLAB Optimization Toolbox</a>. This is needed to refine trajectories with Deep Space Manoeuvres (DSMs), if needed by the user.

These are **suggested** requirements for ASTRA to work to its full potential. Lighter requirements might work well, as ASTRA is able to optimize one launch year at a time, and even one date at a time. The price is the computational time. 

ASTRA **should be** agnostic with respect to the operating system. However, some bugs might arise if Windows is not used.

## Installation Steps

### ASTRA

To work with ASTRA (without any external toolkits), one can simply clone the repository in the local machine:

```bash
git clone "https://github.com/andreabellome/astra"
```

And start using the [tutorials](./usage.md).

In particular, the project structure should be something like the following:

```pgsql
local-folder/
├── ASTRA/
├── clearDeleteAdd.m
└── main_script.m
```

where the script ```clearDeleteAdd.m``` is used to add all the ASTRA functionalities to the working local folder, and it is directly available when downloading the repository from GitHub. The ```main_script.m``` is a generic script that uses ASTRA (e.g., one of the [tutorials](./usage.md)).

### NASA MICE Toolkit

It is suggested to have also the <a href="https://naif.jpl.nasa.gov/naif/toolkit.html" target="_blank">SPICE toolkit</a>. In particular, the MATLAB interface of SPICE is called MICE, and one can download it from <a href="https://naif.jpl.nasa.gov/naif/toolkit_MATLAB.html" target="_blank">here</a>, for different operating systems. This is very useful to integrate high-precision ephemerides of Solar System objects in ASTRA (planets, moons, asteroids, comets...).

Without going too much in detail on MICE, here the steps are reported for a proper integration in ASTRA:

1. Open the <a href="https://naif.jpl.nasa.gov/naif/toolkit_MATLAB.html" target="_blank">toolkit page</a> and select the operating system.
2. Download the zip file ```mice.zip``` for the desired operating system
3. Create a folder called ```MICE_TOOLBOX``` in the main path where ASTRA is and extract there the ```mice.zip```.
4. Then create a folder called ```Kernel``` within ```MICE_TOOLBOX/mice```.
5. Download the required kernels, and add them to the ```Kernel``` folder. We will use the following (link to the NASA repository where to find them):
    <ul>
    <li><a href="https://naif.jpl.nasa.gov/pub/naif/generic_kernels/spk/planets/" target="_blank">de430.bsp</a> -- Solar System planets' ephemerides</li>
    <li><a href="https://naif.jpl.nasa.gov/pub/naif/generic_kernels/spk/satellites/" target="_blank">mar097.bsp</a> -- Mars ephemerides</li>
    <li><a href="https://naif.jpl.nasa.gov/pub/naif/generic_kernels/spk/satellites/a_old_versions/" target="_blank">sat375.bsp</a> -- Saturn ephemerides</li>
    <li><a href="https://naif.jpl.nasa.gov/pub/naif/generic_kernels/pck/" target="_blank">gm_de431.tpc</a> -- gravity constants</li>
    <li><a href="https://naif.jpl.nasa.gov/pub/naif/generic_kernels/lsk/" target="_blank">naif0012.tls</a> -- leapseconds kernel</li>
    <li><a href="https://naif.jpl.nasa.gov/pub/naif/generic_kernels/pck/" target="_blank">pck00010.tpc</a> -- body orientation kernel</li>
    </ul>

6. Within ```MICE_TOOLBOX``` folder, create a makefile called ```data.mk``` like the following:

```makefile
KPL/MK


   \begindata

      PATH_VALUES     = ( './MICE_TOOLBOX/mice/Kernel' )

      PATH_SYMBOLS    = ( 'KERNELS' )

      KERNELS_TO_LOAD = (

                          '$KERNELS/naif0012.tls'
			              '$KERNELS/de430.bsp'
                          '$KERNELS/sat375.bsp'
                          '$KERNELS/mar097.bsp'
                          '$KERNELS/gm_de431.tpc'
                          '$KERNELS/pck00010.tpc'
                        )

   \begintext

End of MK.
```

After all the steps, the final structure of the project should be the following:

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

One now has brand new MICE toolkit ready to be integrated with ASTRA. Different [tutorials]() will show how to use it.
