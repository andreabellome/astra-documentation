# `postProcessOutputASTRA`

## DESCRIPTION
This function processes the output of the ASTRA tool, extracting key information
and organizing it into a structured format for easier analysis and querying.
The processed data includes mission sequences, leg parameters, resonance information,
cost functions, time of flight, Pareto-front solutions, and the path with minimum cost.

## INPUT
- OUTPUT : Structure array containing the raw results from ASTRA, with fields such as:
* minPATH  : Matrix with the path of minimum cost.
* res      : Resonance information (optional).
* LEGS     : Matrix with leg parameters (e.g., departure/arrival times,
velocity values, etc.).
* VAS      : Arrival velocity vectors (km/s).
* VINFa    : Arrival infinity velocities (km/s).
* COSTS    : Cost values for the trajectories (e.g., delta-v in km/s).
* TOFYS    : Time of flight (years).
* ovPF     : Pareto-front solutions.
* minCOST  : Minimum cost value across solutions.
* chosenRevs : Resonance data for each leg.

## OUTPUT
- processed_OUTPUT : Structure containing the processed and reorganized data:
* seq            : Sequence of IDs for the flyby bodies.
* res            : Resonance information (empty if not present).
* LEGS           : Matrix of leg parameters for all solutions.
* VAS            : Arrival velocity vectors (km/s).
* VINFd          : Departure infinity velocities (km/s).
* VINFa          : Arrival infinity velocities (km/s).
* REVS           : Resonance data for all legs.
* depDates       : Departure dates (MJD2000).
* arrDates       : Arrival dates (MJD2000).
* defectsPerLeg  : Defects per leg (km/s) if present, otherwise empty.
* COSTS          : Overall cost function values (km/s).
* TOFYS          : Overall time of flight (years).
* PARETO_FRONT   : Pareto-front solutions.
* LEGSpf         : Leg parameters corresponding to Pareto-front solutions.
* VASpf          : Arrival velocity vectors for Pareto-front solutions.
* VINFapf        : Arrival infinity velocities for Pareto-front solutions.
* REVSpf         : Resonance data for Pareto-front solutions.
* minPATH        : Path corresponding to the minimum cost solution.
* minCOST        : Minimum cost value.
* minTOFY        : Time of flight for the minimum cost solution.
* minVINFd       : Departure infinity velocity for the minimum cost solution.
* minVINFa       : Arrival infinity velocity for the minimum cost solution.
* minREVS        : Resonance data for the minimum cost solution.

## Function Signature
```matlab
[processed_OUTPUT] = postProcessOutputASTRA( OUTPUT )
```
