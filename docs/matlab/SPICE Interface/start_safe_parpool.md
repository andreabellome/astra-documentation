# `start_safe_parpool`

## DESCRIPTION:
Start a parpool safely with physical or logical cores.
If requested number of workers is greater than the physical ones, then
the logical ones are used. If requested number of workers is also greater
than the logical ones, then an error is thrown.

## INPUT:
- nWorkers : number of workers (by default the physical ones)

## OUTPUT:
- pool : MATLAB parpool structure

## Function Signature
```matlab
[pool] = start_safe_parpool(nWorkers)
```
