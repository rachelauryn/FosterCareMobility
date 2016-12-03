import pandas as pd
import numpy as np
import functools as ft
import itertools as it
import matplotlib.pyplot as plt
import scipy.stats
import os
from collections import defaultdict

# convert a pandas series containing indexed data to one representing 
# the PMF and CDF of the data
def get_pmf(series):
    if not type(series) is pd.core.series.Series:
        series = pd.Series(series)
    pmf = series.value_counts().sort_index()
    pmf/=pmf.sum()
    return pmf
def get_cdf(series):
    pmf = get_pmf(series)
    cdf = pmf.cumsum()
    return cdf

# construct a scipy discrete distribution from a pandas Series containing data
# indices will be converted to integers counting from 0
def get_scipy_dist(series):
    pmf = get_pmf(series)
    return scipy.stats.rv_discrete(pmf.iloc[0], pmf.iloc[-1], values=(pmf.index, pmf.values))

# tools for applying the CDF, inverse CDF, and sampling the distribution 
# given a pandas series representing the CDF
def apply_cdf(cdf, x):
    f = lambda x: cdf.iloc[cdf.index.get_loc(x,'pad')]
    if hasattr(x,'__getitem__'):
        return np.vectorize(f)(x)
    return f(x)
def apply_invcdf(cdf, x):
    y = cdf.index[cdf.searchsorted(x)].values
    if not hasattr(x,'__getitem__'):
        y=y[0]
    return y
def sample_cdf(cdf, n):
    return apply_invcdf(cdf, np.random.random(n))