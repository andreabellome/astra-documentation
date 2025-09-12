# `prune_DEFECTtot_DP`

## DESCRIPTION:
This function prunes (removes) trajectory legs based on the total defect value.
It calculates the total defect for each leg and removes those with a total defect exceeding a specified maximum value.

## INPUTS:
LEGSnext : Matrix of trajectory legs, where each row contains details of the legs, including defect values for each segment.
VASnext  : Matrix of velocity vectors associated with each trajectory leg.
VINFnext : Matrix of final velocity norms for each trajectory leg.
defectTOTMax : Maximum allowed total defect value. Legs with a total defect greater than this value will be removed.

## OUTPUTS:
LEGSnext : Updated matrix of trajectory legs after pruning.
VASnext  : Updated matrix of velocity vectors after pruning.
VINFnext : Updated matrix of final velocity norms after pruning.
FUNCTION CALLS:
sum    : Computes the total defect for each trajectory leg by summing over specified columns.
find   : Finds indices of elements that meet the specified condition (total defect > defectTOTMax).

## Function Signature
```matlab
[LEGSnext, VASnext, VINFnext] = prune_DEFECTtot_DP(LEGSnext, VASnext, VINFnext, defectTOTMax)
```
