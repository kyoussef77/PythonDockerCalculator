from scipy.stats import skew
from Statistics.Statistics import *


class Skew:
    @staticmethod
    def skew(data, axis=0, bias=True):
        return skew(data, axis, bias)


