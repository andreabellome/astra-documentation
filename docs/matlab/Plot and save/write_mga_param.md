# `write_mga_param`

## DESCRIPTION
This function generates a formatted text file summarizing a multi-leg interplanetary transfer sequence, including launch conditions, intermediate planetary flybys, and final arrival conditions. It computes and reports hyperbolic excess velocity vectors, launch asymptotic direction, flyby B-plane parameters, and periapsis altitude using ephemerides and planetary constants. The output is structured as a human-readable report suitable for trajectory design analysis and mission documentation.

## INPUT
- struc : Structure array defining the trajectory sequence. Each element contains:
idD [--] departing body ID for leg i
idA [--] arriving body ID for leg i
tD [MJD2000] departure epoch of leg i
tA [MJD2000] arrival epoch of leg i
xxDtar [km, km/s] state vector at departure (position and velocity)
xxAtar [km, km/s] state vector at arrival (position and velocity)
dvA [km/s] arrival impulsive velocity change (optional)
- INPUT : Structure containing global parameters:
idcentral [--] central body identifier
customEphemerides [km, km/s] function handle returning body state;
if not provided defaults to EphSS_cartesian
- name : Output filename string. If relative path is provided, it is
appended to the current working directory; otherwise an absolute
path is used.

## OUTPUT
- out : File identifier of the generated text file containing:
launch conditions (v∞, RA, Dec),
flyby parameters (v∞, B-plane parameters, true anomaly, periapsis
altitude), and arrival conditions (v∞ at target body).

