# `optPSO`

## DESCRIPTION
This function defines and returns the configuration settings for the
Particle Swarm Optimization (PSO) algorithm, based on the provided bounds
for the decision variables. The function allows optional parallel
evaluation of the objective function and sets specific parameters such as
the swarm size, maximum number of iterations, and social adjustment
weight to control the swarm behavior during optimization.

## INPUT
- lb          : lower bounds of the decision variables (1×NVAR vector)
- ub          : upper bounds of the decision variables (1×NVAR vector)
- useParallel : (optional) boolean flag to enable parallel execution of
particleswarm evaluations (default: false)

## OUTPUT
- optionsPSO  : structure containing all the PSO options to be used with
MATLAB's particleswarm optimizer
- NVAR        : number of decision variables inferred from the bounds
- MAXIT       : maximum number of PSO iterations

## Function Signature
```matlab
[optionsPSO, NVAR, MAXIT] = optPSO(lb, ub, useParallel)
```
