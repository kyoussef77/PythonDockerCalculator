from StatisticsOperations.mean import Mean
from StatisticsOperations.mode import Mode
from StatisticsOperations.median import Median
from StatisticsOperations.variance import Variance
from StatisticsOperations.stand_dev import Stand_dev
from StatisticsOperations.quartiles import Quantile
from StatisticsOperations.skew import Skew
from StatisticsOperations.correlation import Correlation
from StatisticsOperations.zscore import Zscore


def mean(data):
    return Mean.mean(data)


def mode(data):
    return Mode.mode(data)


def median(data):
    return Median.median(data)


def variance(data):
    return Variance.variance(data)


def st_dev(data):
    return Stand_dev.stdev(data)


def quartile(data, q, axis, kdims):
    return Quantile.quartile(data, q, axis, kdims)


def skew(data, axis, bias):
    return Skew.skew(data, axis, bias)


def SampleCor(data1, data2):
    return Correlation.SampleCor(data1, data2)


def PopulationCor(data1, data2):
    return Correlation.PopulationCor(data1, data2)


def zscore(data):
    return Zscore.zscore(data)