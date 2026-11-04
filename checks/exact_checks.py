"""Exact checks of the Legendre identities and sample negative Hankel minors."""
import sympy as S
from math import comb
import json
from pathlib import Path
z,a,b,y,t,u,v=S.symbols('z a b y t u v',real=True)
# The product-formula RHS is polynomial; even cosine moments remove root choices.
for n in range(13):
 P=S.Poly(S.legendre(n,y),y)
 rhs=0
 for (j,),coeff in P.terms():
  for k in range(0,j+1,2):
   rhs+=coeff*comb(j,k)*(a*b)**(j-k)*((a*a-1)*(b*b-1))**(k//2)*S.Rational(comb(k,k//2),2**k)
 assert S.expand(rhs-S.legendre(n,a)*S.legendre(n,b))==0
for n in range(31):
 assert S.expand(S.legendre(n,1+2*z)-sum(comb(n,k)*comb(n+k,k)*z**k for k in range(n+1)))==0
# Critical endpoint expansion r=1/2, v=0.
lo=2+2*S.cos(S.pi+u)-2*S.sqrt(S.Rational(5,4)+S.cos(S.pi+u))
assert S.series(lo,u,0,6).removeO()==-1+u**4/2
# Classical Legendre orthogonality, enough to check Poisson moments via its series.
for n in range(9):
 for m in range(9):
  q=S.integrate(S.legendre(n,y)*S.legendre(m,y),(y,-1,1))
  assert q==(S.Rational(2,2*n+1) if n==m else 0)
# Negative Hankel minors at sample parameters, in exact arithmetic.
controls=[]
for x in [S.Rational(1,100),S.Rational(1,4),S.Rational(1,2)]:
 vals=[sum(comb(n,k)**2*comb(n+k,k)**2*x**k for k in range(n+1)) for n in range(31)]
 found=None
 for N in range(2,16):
  for off in (0,1):
   DM=S.polys.matrices.DomainMatrix.from_Matrix(S.Matrix(N,N,lambda i,j:vals[i+j+off]))
   d=DM.domain.to_sympy(DM.det())
   if d<0:
    found={'x':str(x),'size':N,'shift':off,'determinant':str(d)};break
  if found:break
 controls.append(found or {'x':str(x),'no_negative_minor_through':15})
out={'product_formula_checked_degrees':list(range(13)),'binomial_legendre_checked_degrees':list(range(31)),'critical_quartic_coefficient':'1/2','orthogonality_degrees':list(range(9)),'negative_minor_controls':controls}
Path(__file__).with_name('EXACT_CHECKS.json').write_text(json.dumps(out,indent=2))
print(json.dumps(out,indent=2))
