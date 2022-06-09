import numpy as np
from lmfit import Model
from sklearn.metrics import r2_score


def ref_rsq(p,d):
    dp1 = np.polyfit(p.wvl(d)[6], p.itst(d)[6], 4)
    f1 = np.poly1d(dp1)
    ref_rsq = r2_score(p.itst(d)[6], f1(p.wvl(d)[6]))
    return ref_rsq

def IV_left_rsq(a,b,d):
    v1 = a.v(d)[:10]
    i1 = a.i(d)[:10]
    lmodel = Model(b.eq)
    params1 = lmodel.make_params(a=1, b=1, c=1, d=1, e=1)
    result1 = lmodel.fit(i1, params1, x=v1)
    IV_left_rsq = r2_score(i1, result1.best_fit)
    return IV_left_rsq

def IV_right_rsq(a,b,d):
    v2 = a.v(d)[9:]
    i2 = a.i(d)[9:]
    rmodel = Model(b.IV)
    result2 = rmodel.fit(i2, x=v2, q=1, w=1, alp=1, v=v2, i=i2)
    IV_right_rsq = r2_score(i2, result2.best_fit)
    return IV_right_rsq
