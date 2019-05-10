# -*- coding: utf-8 -*-
"""
Created on Thu May  9 14:13:43 2019

@author: UNR Math Stat
"""

import numpy
import pandas
import math
import matplotlib
from matplotlib import pyplot

DF = pandas.read_excel('SP500StocksCap.xlsx')
data = DF.values
NSTOCKS = numpy.size(data, 0)

for k in numpy.arange(1, 121, 12):
    caps = data[:, k]
    updatedCaps  = []
    for item in caps:
        if not numpy.isnan(item):
            updatedCaps.append(item)
    rankedCaps = sorted(updatedCaps)
    rankedCaps = rankedCaps[::-1]
    totalCap = sum(rankedCaps)
    logCap = math.log(totalCap)
    NSTOCKS = numpy.size(rankedCaps)
    logRanks = numpy.array([math.log(k+1) for k in range(NSTOCKS)])
    logCaps = numpy.array([math.log(item) - logCap for item in rankedCaps])
    pyplot.plot(logRanks, logCaps)
pyplot.show