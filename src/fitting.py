import numpy as np


def eq(x, a, b, c, d, e):
    return a * (x**4) + b * (x**3) + c * (x**2) + d*x + e

def IV(x, q, w, alp, v = [], i = []):
    polyfiti = np.polyfit(v, i, 6)
    fiti = np.poly1d(polyfiti)
    return abs(q*(np.exp(x/w)-1))+alp*fiti(x)

