"""Exact Bernstein sign certificates for the negative Hankel minors."""
from pathlib import Path
import json
import sympy as s
from sympy.polys.matrices import DomainMatrix
ROOT=Path(__file__).resolve().parent
x=s.symbols('x')
A=[sum(s.binomial(n,k)**2*s.binomial(n+k,k)**2*x**k for k in range(n+1)) for n in range(19)]
windows=[(4,0,s.Rational(0),s.Rational(9,100)),(8,0,s.Rational(1,20),s.Rational(101,500)),(9,1,s.Rational(201,1000),s.Rational(47,100)),(10,0,s.Rational(41,100),s.Rational(2,3))]
expected={(4,0):(3,9),(8,0):(14,42),(9,1):(18,63),(10,0):(23,67)}
out=[]
for d,shift,a,b in windows:
 D=DomainMatrix.from_Matrix(s.Matrix(d,d,lambda i,j:A[i+j+shift]))
 p=s.Poly(D.domain.to_sympy(D.det()),x)
 valuation=min(m[0][0] for m in p.terms())
 q=s.Poly(p.as_expr()/x**valuation,x);n=q.degree()
 assert (valuation,n)==expected[d,shift]
 power=s.Poly(q.as_expr().subs(x,a+(b-a)*x).expand(),x)
 coeff=[sum(power.nth(j)*s.binomial(k,j)/s.binomial(n,j) for j in range(k+1)) for k in range(n+1)]
 assert all(c<0 for c in coeff)
 # Rebuild the polynomial from its Bernstein coefficients.
 reconstruction=sum(coeff[k]*s.binomial(n,k)*x**k*(1-x)**(n-k) for k in range(n+1))
 assert s.Poly(reconstruction-power.as_expr(),x).is_zero
 out.append({'size':d,'shift':shift,'interval':[str(a),str(b)],'x_valuation':valuation,'reduced_degree':n,'reduced_polynomial_coefficients':[str(c) for c in q.all_coeffs()],'bernstein_coefficients':[str(c) for c in coeff],'all_strictly_negative':True,'basis_reconstruction':True})
(ROOT/'BERNSTEIN_CERTIFICATE.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps([{k:v for k,v in row.items() if 'coefficients' not in k} for row in out],indent=2))
