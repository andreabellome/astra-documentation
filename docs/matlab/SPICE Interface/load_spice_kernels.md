# `load_spice_kernels`

## DESCRIPTION:
This function clears any previously loaded SPICE kernels and loads a
user-specified meta-kernel. It is primarily intended for use inside
parallel workers, where each worker needs to load SPICE kernels
independently. The function returns a boolean flag indicating whether
the kernel loading operation was successful.

## INPUT:
- path_to_data_metakernel : full path to a SPICE meta-kernel (.tm or .mk)
that lists all kernels to be loaded.

## OUTPUT:
- out : logical flag:
true  → kernels loaded successfully
false → an error occurred while loading kernels

## Function Signature
```matlab
[out] = load_spice_kernels( path_to_data_metakernel )
```
