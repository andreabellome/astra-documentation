# `prune_VINFn_DP`

## DESCRIPTION:
This function prunes the possible trajectory legs based on specified limits for the incoming velocity (`VINF`).
It removes any trajectory legs where the incoming velocity falls outside the specified range.

## INPUT:
- LEGSnext : Matrix containing the possible trajectory legs, where each row represents a leg with columns
for departure and arrival planets, departure and arrival times, and the delta-v required.
- VASnext  : Matrix containing the arrival velocities at the destination planets for each leg.
- VINFnext : Vector containing the incoming velocities at the destination planets for each leg.
- vinflim  : Matrix specifying the minimum and maximum allowable incoming velocities for each planet in the sequence.

## OUTPUT:
- LEGSnext : Matrix with trajectory legs that have incoming velocities outside the specified limits removed.
- VASnext  : Matrix with corresponding rows removed from the arrival velocities.
- VINFnext : Vector with corresponding entries removed from the incoming velocities.

## Function Signature
```matlab
[LEGSnext, VASnext, VINFnext] = prune_VINFn_DP(LEGSnext, VASnext, VINFnext, vinflim)
```
