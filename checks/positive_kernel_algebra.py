"""Exact checks of the elliptic-kernel factorizations and derivative signs."""
from pathlib import Path
import sympy as s,json
r,d,y=s.symbols('r d y',positive=True)
m=(d*d-1)/(2*r)
A=(1-d)**2-m*m;B=(1+d)**2-m*m
assert s.factor(A-(d-1)**2*(1-(d+1)**2/(4*r*r)))==0
assert s.factor(B-(d+1)**2*(1-(d-1)**2/(4*r*r)))==0
assert s.factor(B-A-4*d)==0
Ah=s.factor((s.diff(A,d)/(4*d)).subs(d,2*r-1))
BH=s.factor((s.diff(B,d)/(4*d)).subs(d,2*r+1))
assert s.factor(Ah+(r-1)**2/(r*(2*r-1)))==0
assert s.factor(BH+(r+1)**2/(r*(2*r+1)))==0
e=s.symbols('e')
near=s.series(A.subs(d,s.sqrt(1+e/2)),e,0,3).removeO()
assert s.factor(near-(1-r**-2)*e**2/16)==0
out={'A_factorization':str(s.factor(A)),'B_factorization':str(s.factor(B)),
     'B_minus_A':'4*d','A_derivative_at_h':str(Ah),
     'B_derivative_at_H':str(BH),'A_double_zero_coefficient':str((1-r**-2)/16),
     'status':'Exact symbolic identities passed; analytic continuation is addressed separately in the manuscript.'}
Path(__file__).with_name('EXACT_ALGEBRA_CHECKS.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
