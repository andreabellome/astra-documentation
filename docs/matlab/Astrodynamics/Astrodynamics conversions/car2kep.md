# `car2kep`

## INPUT:
in[6]       State vector in cartesian coordinates (position [L],
velocity [L/T]).
mu          Planetary gravity constant [L^3/(M*T^2)].

## OUTPUT:
kep[1,6]    Vector of Keplerian elements: kep = [a, e, i, Om, om, th],
where theta is the true anomaly. a in [L],
0 <= i  <= pi   [rad]
0 <= Om <  2*pi [rad]
0 <= om <  2*pi [rad]
0 <= th <  2*pi [rad].
p           Parameter [L].
E           Eccentric anomaly, hyperbolic anomaly or parabolic anomaly
(for definitions see Vallado pag. 49).
M           Mean anomaly [rad].
dt          Time from the pericentre passage [T].
Threshold on eccentricity for considering the orbit to be circular
Value determined comparing the relative error on state and position
between using the circular case and the elliptic case. With this elimit
the relative error on position and velocity is always less then 1e-7.
Angular momentum vector: h = cross(r,v)
Inclination
Line of nodes vector
% n = cross([0 0 1],h);
% Normalisation of nv to 1: n = n/norm(n)
%                           n = n/sqrt(n(1)^2+n(2)^2+n(3)^2);
% Arbitrary choice of n
warning('spaceToolbox:car2kep:planarOrbit','Planar orbit. Arbitrary choice of Omega = 0.');
Argument of the ascending node
Parameter
Eccentricity vector: ev = 1/mu*cross(v,h) - r/nr
ev  = 1/mu*[v(2)*h(3)-v(3)*h(2),v(3)*h(1)-v(1)*h(3),v(1)*h(2)-v(2)*h(1)] - r/nr;
Argument of the pericentre
% Arbitrary eccentricity vector
Semi-major axis
True anomaly: acos(dot(ev,r)/ne/nr);
% the condition dot(r,cross(h,ev)) < 0 works in the same way

## Function Signature
```matlab
[kep] = car2kep(in,mu)
```
