from Calculator.Calculator import Calculator
from Statistics.mean import Mean

from MathOperations.random import Random_num;

class Statistics(Calculator):

    def mean(self, data):
        self.Result = Mean(data)
        return self.Result


    def Random_int_nums(self, a, b, c, d):
        self.Result = Random_num.random_int_generator(a,b,c,seed_num=d)
        return self.Result

    def Random_float_nums(self, a, b, c, d):
        self.Result = Random_num.random_float_generator(a, b, c, seed_num=d)
        return self.Result