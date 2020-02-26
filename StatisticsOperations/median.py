from MathOperations.addition import Addition
from MathOperations.division import Division

class Median:
    @staticmethod
    def median(data):
        length = len(data)
        s_data = sorted(data)

        if length % 2 == 0:
            median1 = s_data[length // 2]
            median2 = s_data[length // 2 - 1]
            median = Division.quotient(Addition.sum(median1,median2), 2)
            return median
        else:
            median = s_data[length // 2]
            return median
