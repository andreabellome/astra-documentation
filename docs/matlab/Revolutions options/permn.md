# `permn`

## EXAMPLES:
M = permn([1 2 3],2) % returns the 9-by-2 matrix:
1     1
1     2
1     3
2     1
2     2
2     3
3     1
3     2
3     3
M = permn([99 7],4) % returns the 16-by-4 matrix:
99     99    99    99
99     99    99     7
99     99     7    99
99     99     7     7
...
7      7     7    99
7      7     7     7
M = permn({'hello!' 1:3},2) % returns the 4-by-2 cell array
'hello!'        'hello!'
'hello!'        [1x3 double]
[1x3 double]    'hello!'
[1x3 double]    [1x3 double]
V = 11:15, N = 3, K = [2 124 21 99]
M = permn(V, N, K) % returns the 4-by-3 matrix:
%        11  11  12
%        15  15  14
%        11  15  11
%        14  15  14
% which are the 2nd, 124th, 21st and 99th permutations
% Check with PERMN using two inputs
M2 = permn(V,N) ; isequal(M2(K,:),M)
% Note that M2 is a 125-by-3 matrix
% PERMN can be used generate a binary table, as in
B = permn([0 1],5)
NB Matrix sizes increases exponentially at rate (n^N)*N.
See also PERMS, NCHOOSEK
ALLCOMB, PERMPOS, NEXTPERM, NCHOOSE2 on the File Exchange
tested in Matlab 2018a
version 6.2 (jan 2019)
(c) Jos van der Geest
Matlab File Exchange Author ID: 10584
email: samelinoa@gmail.com
%% PERMN(V,N) - return all permutations
% return column vectors
% this is faster than the math trick used with 3 inputs below
%% PERMN(V,N,K) - return a subset of all permutations
% The engine is based on version 3.2 with the correction
% suggested by Roger Stafford. This approach uses a single matrix
% multiplication.
Algorithm using for-loops
which can be implemented in C or VB
nv = length(V) ;
C = zeros(nv^N,N) ; % declaration
for ii=1:N,
cc = 1 ;
for jj=1:(nv^(ii-1)),
for kk=1:nv,
for mm=1:(nv^(N-ii)),
C(cc,ii) = V(kk) ;
cc = cc + 1 ;
end
end
end
end

## Function Signature
```matlab
[M, I] = permn(V, N, K)
```
