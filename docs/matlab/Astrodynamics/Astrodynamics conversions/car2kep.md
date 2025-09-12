# `car2kep`

## DESCRIPTION:
Convert cartesian elements into keplerian elements.

## INPUT:
- in[6] :       State vector in cartesian coordinates (position [L],
velocity [L/T]).
- mu :           Planetary gravity constant [L^3/(M*T^2)].

## OUTPUT:
- kep[1,6] :    Vector of Keplerian elements: kep = [a, e, i, Om, om, th],
where theta is the true anomaly. a in [L],
0 <= i  <= pi   [rad]
0 <= Om <  2*pi [rad]
0 <= om <  2*pi [rad]
0 <= th <  2*pi [rad].
- p :            Parameter [L].
- E :           Eccentric anomaly, hyperbolic anomaly or parabolic anomaly
(for definitions see Vallado pag. 49).
- M :           Mean anomaly [rad].
- dt :          Time from the pericentre passage [T].

## Function Signature
```matlab
[kep] = car2kep(in,mu)
```
