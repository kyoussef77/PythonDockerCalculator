from Calculator.Calculator import Calculator
from StatisticsOperations.mean import Mean
from StatisticsOperations.mode import Mode
from StatisticsOperations.median import Median
from Random.random_Op import Random_num;


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