"""Continue the elliptic germ by its ODE along two upper paths.

The connection formulas from the paper are used only in the final comparison.
"""
import cmath
import json
import math
from pathlib import Path
import mpmath as mp
import numpy as np
from scipy.integrate import solve_ivp


def data(d, r):
    m = (d*d-1)/(2*r)
    b = (1+d)**2-m*m
    db = 2*(1+d)-2*m*d/r
    p = 4*d/b
    dp = 4/b-4*d*db/(b*b)
    return b, db, p, dp


def continued(r, end, height, tolerance):
    start = math.sqrt(.5)
    b, _, p, _ = data(start, r)
    k = float(mp.ellipk(p))
    kp = float(mp.ellipe(p)/(2*p*(1-p))-mp.ellipk(p)/(2*p))
    state = np.array([k, kp, cmath.sqrt(b)], dtype=complex)
    path = [start, start+1j*height, end+1j*height, end]
    for a, z in zip(path, path[1:]):
        delta = z-a
        def rhs(s, v):
            b, db, p, dp = data(a+delta*s, r)
            return delta*np.array([v[1]*dp,
                ((2*p-1)*v[1]+.25*v[0])/(p*(1-p))*dp,
                db/(2*b)*v[2]])
        sol = solve_ivp(rhs, (0,1), state, method='DOP853',
                        rtol=tolerance, atol=tolerance*.01)
        assert sol.success, sol.message
        state = sol.y[:,-1]
    return state[0]/state[2]/(2*math.pi**2*r)


def bank(r, d):
    m = (d*d-1)/(2*r)
    a, b = (1-d)**2-m*m, (1+d)**2-m*m
    c = 1/(2*math.pi**2*r)
    if d < 2*r-1:
        p = 4*d/b
        return c/math.sqrt(b)*complex(mp.ellipk(p), 2*mp.ellipk(1-p))
    if d < 2*r+1:
        q = b/(4*d)
        return c/math.sqrt(4*d)*complex(mp.ellipk(q), 3*mp.ellipk(1-q))
    t = b/a
    return c/math.sqrt(-a)*complex(-2*mp.ellipk(t), 3*mp.ellipk(1-t))


rows = []
for r in [1.01, 1.1, 2., 10.]:
    for interval, d in enumerate([r, 2*r, 2*r+2], 1):
        expected = bank(r,d)
        for height in [.2, .6]:
            loose = continued(r,d,height,1e-9)
            tight = continued(r,d,height,2e-12)
            error = abs(tight-expected)/abs(expected)
            assert error < 2e-8, (r,d,height,tight,expected,error)
            rows.append(dict(r=r,d=d,interval=interval,height=height,
                relative_error=error,tolerance_change=abs(tight-loose)/abs(expected)))
out = dict(status='PASS: floating-point ODE diagnostic only',
    method='Hypergeometric ODE continuation from y=0; two upper paths and tolerances',
    rows=rows, maximum_relative_error=max(row['relative_error'] for row in rows))
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
