# `getSPK`

## DESCRIPTION
This function retrieves a Spacecraft and Planet Kernel (SPK) file from NASA's
Horizons API for a specified object and time range, saving it to a given directory.
If a file with the same name already exists, the function either overwrites it
(if the overwrite flag is set) or stops execution with a warning.

## INPUT
- spk_id  : string specifying the SPK ID of the target object.
- date_i  : string specifying the start date for the SPK file in a format
accepted by the Horizons API.
- date_f  : string specifying the end date for the SPK file in a format
accepted by the Horizons API.
- spk_dir : string specifying the directory where the SPK file should be saved.
If empty, the file is saved in the current directory.
- varargin: optional parameters:
'overwrite', 'on'  -> Overwrites an existing SPK file.
'overwrite', 'off' -> Prevents overwriting (default).
'warning', 'on'    -> Displays a warning if the file exists (default).
'warning', 'off'   -> Suppresses warnings if the file exists.

## OUTPUT
- success : binary flag indicating success (1) or failure (0) in retrieving and
saving the SPK file.

## Function Signature
```matlab
[success] = getSPK(spk_id,date_i,date_f,spk_dir,varargin)
```
