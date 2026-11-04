"""Exact algebra for the continuation of the elliptic density."""
import sympy as s
r,d,z=s.symbols('r d z', nonzero=True)
m=(d*d-1)/(2*r)
A=(1-d)**2-m*m
B=(1+d)**2-m*m
assert s.factor(A-(d-1)**2*(1-(d+1)**2/(4*r*r)))==0
assert s.factor(B-(d+1)**2*(1-(d-1)**2/(4*r*r)))==0
assert s.expand(B-A-4*d)==0
h=1+8*r*r-8*r
H=1+8*r*r+8*r
for root, image in [(0,-1),(1,1),(-1,1),(2*r-1,h),(-2*r-1,H),(1+2*r,H),(1-2*r,h)]:
 assert s.expand(2*root**2-1-image)==0
Az=-z*z/(16*r*r)+(s.Rational(1,2)+1/(8*r*r))*z+s.Rational(3,2)-1/(16*r*r)-2*d
assert s.factor(Az.subs(z,2*d*d-1)-A)==0
print('PASS: factors, all projected finite singularities, B-A, large-z expansion. Exact symbolic checks; analytic bounds are proved in the note.')
