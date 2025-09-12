# `seq2SeqName`

## DESCRIPTION
This function converts a sequence of planet or celestial body IDs into a concatenated
string representing the sequence by name. If the ID corresponds to a known planet,
its name is retrieved and added to the sequence name; otherwise, the ID itself is
used as a string.

## INPUT
- seq : Array of integers representing the sequence of planet or celestial body IDs.
- idcentral : ID of the central body. See constants.m

## OUTPUT
- seqName : A string representing the concatenated names of the planets or IDs in the sequence.

## Function Signature
```matlab
[seqName] = seq2SeqName(seq, idcentral)
```
