# `generateDiffRuns`

## DESCRIPTION:
This function processes a matrix of revision codes and generates a corresponding matrix of revision options.
It also optionally appends additional data to the output matrix based on the input `res`.

## INPUTS:
revVec : Matrix of revision codes. Each element specifies a different revision type.
res     : (Optional) Matrix of results, where the last column indicates which legs are being referenced.

## OUTPUT
REVS is structured as follows:
- Each row corresponds to a revision code and its mapped options.
- Additional columns are appended if `res` is provided, based on the legs results.
EXAMPLES:
If `revVec` is [10; 21; 30] and `res` is [1 2; 3 4; 5 6], the output `REVS` will include the mapped options and potentially additional columns from `res`.
PROCESSING STEPS:
1. Initialize `REVS` with zeroes.
2. Map revision codes to options.
3. Optionally append additional data from `res` based on leg results.

## OUTPUT:
REVS    : Matrix of revision options, with each revision code mapped to a specific option set.
Optionally includes data from `res` if `res` is provided.
PROCESS:
1. Reshape `res` to have 3 rows and adjust it for processing.
2. Extract the last column of `res` which represents legs results.
3. Initialize a variable to track the column index for revision options.
4. Loop through each element of `revVec` to map the revision codes to option sets:
- 0  -> [0 0]
- 10 -> [1 0]
- 11 -> [1 1]
- 20 -> [2 0]
- 21 -> [2 1]
- 30 -> [3 0]
- 31 -> [3 1]
5. Append two zero columns to `REVS` for possible additional data.
6. If `res` is provided, append the data from `res` to the last two columns of `REVS`.

## Function Signature
```matlab
[REVS] = generateDiffRuns(revVec, res)
```
