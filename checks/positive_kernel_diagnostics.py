"""High-precision checks of the dispersion formula."""
from pathlib import Path
import mpmath as m,json
m.mp.dps=35
results=[]
for r0,y0 in [('1.1','0'),('2','-1'),('2','0'),('2','0.5'),('10','0')]:
 r=m.mpf(r0);y=m.mpf(y0);h=1+8*r*r-8*r;H=1+8*r*r+8*r
 def rho(a):
  d=m.sqrt((a+1)/2);A=(1-d)**2-(a-1)**2/(16*r*r);B=(1+d)**2-(a-1)**2/(16*r*r)
  if a<h:v=2*m.elliprf(0,4*d,abs(B))
  elif a<H:v=3*m.elliprf(0,4*d,abs(B))
  else:v=3*m.elliprf(0,abs(A),abs(B))
  return v/(2*m.pi**3*r)
 d=m.sqrt((y+1)/2);A=(1-d)**2-(y-1)**2/(16*r*r);B=(1+d)**2-(y-1)**2/(16*r*r)
 direct=m.elliprf(0,A,B)/(2*m.pi**2*r)
 dispersion=m.quad(lambda a:rho(a)/(a-y),[1,h,H,2*H,10*H,m.inf])
 error=abs(direct-dispersion)
 assert error<m.mpf('1e-25')
 results.append({'r':r0,'y':y0,'direct_elliptic':m.nstr(direct,28),'dispersion_integral':m.nstr(dispersion,28),'absolute_error_below_1e-25':True})
out={'status':'Non-interval numerical diagnostics passed; not a proof','mpmath_precision':35,'results':results}
Path(__file__).with_name('POSITIVE_KERNEL_DIAGNOSTICS.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
