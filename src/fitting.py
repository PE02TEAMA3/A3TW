# import xml.etree.ElementTree as ET
# import matplotlib.pyplot as plt
# import numpy as np
# from numpy import exp
# from lmfit import Model
# from sklearn.metrics import r2_score
# import time
# import pandas as pd

def IV(x, Is, q, n, k):
    return Is * (exp((q * x) / (n * k)) - 1)

def IVfitting(x, q, w, alp, xi = [], yi = []):
    polyfiti = np.polyfit(xi, yi, 12)
    fiti = np.poly1d(polyfiti)
    return abs(q*(np.exp(x/w)-1))+alp+fiti(x)