from scipy.stats import pearsonr
from numpy import corrcoef

class Correlation:

    @staticmethod
    def SampleCor(data1,data2):
        return pearsonr(data1,data2)

    @staticmethod
    def PopulationCor(data1,data2):
        return corrcoef(data1,data2)
