from Calculator.Calculator import Calculator
from StatisticsOperations.StatisticsOperations import *


class Statistics(Calculator):

    def mean(self, data):
        self.Result = Mean.mean(data)
        return self.Result

    def mode(self, data):
        self.Result = Mode.mode(data)
        return self.Result

    def median(self, data):
        self.Result = Median.median(data)
        return self.Result

    def variance(self, data):
        self.Result = Variance.variance(data)
        return self.Result

    def st_dev(self, data):
        self.Result = Stand_dev.stdev(data)
        return self.Result

    def quartile(self, data, q, axis, kdims):
        self.Result = Quantile.quartile(data, q, axis, kdims)
        return self.Result

    def skew(self, data, axis, bias):
        self.Result = Skew.skew(data, axis, bias)
        return self.Result

    def SampleCor(self, data1, data2):
        self.Result = Correlation.SampleCor(data1, data2)
        return self.Result

    def PopulationCor(self, data1, data2):
        self.Result = Correlation.PopulationCor(data1, data2)
        return self.Result

    def zscore(self, data):
        self.Result = Zscore.zscore(data)
        return self.Result