# `generateOutputTXT`

## DESCRIPTION
This function generates a text file containing detailed information about
a trajectory path, including departure and arrival planets, v-infinity
velocities, transfer types, and additional trajectory metrics.

## INPUT
- path   : Matrix where each row represents a state in the trajectory with
columns for position (x, y, z), velocity (vx, vy, vz),
planetary ID, time, and v-infinity information.
- folder : (Optional) Directory path where the output text file will be saved.
If not specified, the file is saved in the "results" folder or
created if it doesn't exist.
- nametemp : (Optional) Name of the output text file. If not specified,
a default name based on the trajectory sequence is used.

## OUTPUT
- out    : A file handle to the created text file containing the trajectory
details and metrics formatted as specified.

## Function Signature
```matlab
[out] = generateOutputTXT(path, idcentral, customEphemerides, folder, nametemp)
```
