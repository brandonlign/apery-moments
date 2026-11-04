"""Numerical checks of the continued branches around large circles."""
import mpmath as m
import json
m.mp.dps=65
rows=[]
for r in map(m.mpf,['1.001','1.1','2','10']):
 R=1000*r*r
 worst=m.mpf(0)
 for j in range(33):
  theta=m.pi*j/32
  z=R*m.exp(1j*theta)
  d=m.sqrt((z+1)/2)
  A=(1-d)**2-((z-1)/(4*r))**2
  e=-16*r*r*A/z**2-1
  w=-4*d/A
  logw=m.log(64*r*r/m.sqrt(2))-m.mpf('1.5')*(m.log(R)+1j*theta)+m.log(1+1/z)/2-m.log(1+e)
  G=m.fsum([(m.rf(m.mpf('.5'),n)/m.factorial(n))**2*(m.digamma(n+1)-m.digamma(n+m.mpf('.5')))*w**n for n in range(50)])
  K=m.ellipk(w)
  f=((2/m.pi)*K*logw-2*G+3j*K)/(2*m.pi**2*r*(z/(4*r)*m.sqrt(1+e)))
  bound=m.sqrt(32)/(2*m.pi**2*R)*(m.sqrt(2)*(m.mpf('1.5')*m.log(R)+5)+8*m.log(2)+3*m.pi/m.sqrt(2))
  worst=max(worst,abs(f)/bound)
  assert abs(f)<=bound
  assert abs(w)<m.mpf('.5')
  assert abs(logw.imag)<5
  if j==32:
   assert abs(f.imag)<m.mpf('1e-45')
   assert f.real>0
   negative=f.real
 rows.append({'r':str(r),'R':str(R),'max_observed_bound_ratio':str(worst),'negative_axis_value':str(negative)})
print(json.dumps({'status':'PASS non-interval diagnostics only','angles_per_parameter':33,'rows':rows},indent=2))
