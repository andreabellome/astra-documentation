# `rev2RevOpt`

## DESCRIPTION
This function is used to generate options for Lambert problem Number of
revolutions and case (low-/high- energy).

## INPUT
- rev : number encoding number of revolutions and case for Lambert
problem. For example:
rev = 0  --> means 0 revs.
rev = 10 --> means 1 rev. and case 0 (low energy)
rev = 11 --> means 1 rev. and case 1 (high energy)
rev = 20 --> means 2 revs. and case 0 (low energy)
rev = 21 --> means 2 revs. and case 1 (high energy)
and so on...
- res : 1x3 vector with N:M resonant ratio and number of leg at which the
resonant transfer is needed. If no resonant transfer is needed,
leave it empty.
- indleg : ID of the current leg.

## OUTPUT
- revopt : 1x4 vector with the following info:
- revopt(1:2) is for number of revolutions and case for
Lambert problem solution.
- revopt(3:4) is for resonant ratio, if present: then
revopt(1:2) = 0. If not present, revopt(3:4) = 0.

## Function Signature
```matlab
[revopt] = rev2RevOpt(rev, res, indleg)
```
