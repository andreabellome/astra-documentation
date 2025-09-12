# `ASTRA_dates`

## DESCRIPTION
This function uses SODP (Single Objective Direct Problem) to find the
optimal trajectory for a spacecraft given a range of launch dates.
It iteratively computes the trajectory and cost for each launch date,
then post-processes the results to determine the minimum cost trajectory.

## INPUT
- INPUT : structure containing mission parameters, including launch date
options, plotting options, and other necessary configurations.
- seq   : sequence of IDs for flyby bodies (see constants.m)

## OUTPUT
- OUTPUT : structure array containing the computed trajectories and their
associated costs for each considered launch date.

## Function Signature
```matlab
[OUTPUT] = ASTRA_dates(INPUT, seq)
```
