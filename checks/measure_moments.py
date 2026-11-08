"""Compare Legendre moments of the angular density with its positive Q_n mixture.

Q_n is evaluated by a hypergeometric formula, separately from the change of
variables used to build the representing measure.
"""
from pathlib import Path
import json
import mpmath as mp

mp.mp.dps = 40


def parameters(y, r):
    d = mp.sqrt((y + 1) / 2)
    # Rationalized differences retain precision near y=1 and y=H.
    a = ((y - 1)/(2*(d + 1)))**2 * (1 - (d + 1)**2/(4*r*r))
    upper = 1 + 8*r*r + 8*r
    b = ((d + 1)**2*(upper - y)*(2*r - 1 + d) /
         (8*r*r*(2*r + 1 + d)))
    return d, a, b


def angular_density(y, r):
    if y == 1:
        return mp.mpf(0)  # A value at one logarithmic endpoint does not affect the integral.
    _, a, b = parameters(y, r)
    return mp.elliprf(0, a, b) / (2*mp.pi**2*r)


def spectral_density(y, r):
    d, a, b = parameters(y, r)
    h, upper = 1 + 8*r*r - 8*r, 1 + 8*r*r + 8*r
    if y == upper:
        return mp.mpf(0)  # Quadrature may round a node onto the logarithmic endpoint.
    if y < upper:
        coefficient = 2 if y < h else 3
        rf = mp.elliprf(0, 4*d, b)
    else:
        coefficient = 3
        rf = mp.elliprf(0, -a, -b)
    return coefficient * rf / (2*mp.pi**3*r)


def q_function(n, a):
    if a == 1:
        return mp.mpf(0)  # The integrable endpoint is excluded from the open domain.
    return (mp.sqrt(mp.pi)*mp.factorial(n) /
            (mp.gamma(n + mp.mpf('1.5'))*(2*a)**(n+1)) *
            mp.hyp2f1(mp.mpf(n+1)/2, mp.mpf(n+2)/2,
                       n + mp.mpf('1.5'), 1/(a*a)))


rows = []
for r in map(mp.mpf, ['1.1', '2', '10']):
    h, upper = 1 + 8*r*r - 8*r, 1 + 8*r*r + 8*r
    for n in [0, 1, 2, 4]:
        direct = mp.quad(lambda y: mp.legendre(n, y)*angular_density(y, r),
                         [-1, 0, 1])
        mixture = 2*mp.quad(lambda a: spectral_density(a, r)*q_function(n, a),
                            [1, h, upper, mp.inf])
        error = abs(direct - mixture)
        assert error < mp.mpf('1e-25'), (r, n, direct, mixture, error)
        rows.append(dict(r=str(r), n=n, direct=mp.nstr(direct, 32),
                         positive_mixture=mp.nstr(mixture, 32),
                         absolute_error=mp.nstr(error, 8)))

report = dict(precision_digits=mp.mp.dps, tolerance='1e-25',
              maximum_absolute_error=mp.nstr(max(mp.mpf(x['absolute_error']) for x in rows), 8),
              comparisons=rows)
Path(__file__).with_name('MEASURE_MOMENTS.json').write_text(
    json.dumps(report, indent=2) + '\n')
print(json.dumps(report, indent=2))
