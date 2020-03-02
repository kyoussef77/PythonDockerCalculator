import unittest
from Statistics.Statistics import Statistics


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.statistics = Statistics()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.statistics, Statistics)

    def test_decorator_calculator(self):
        self.assertIsInstance(self.statistics, Statistics)

    # Test Mean -------------------------------------------------------------
    def test_statistics_calculator_return_mean(self):
        data = [1, 2, 3, 4, 5]
        result = self.statistics.mean(data)
        self.assertEqual(3, result)

    # Test Mean -------------------------------------------------------------

    # Test Mode -------------------------------------------------------------
    def test_statistics_calculator_return_mode(self):
        data = [1, 2, 3, 3, 4, 5]
        result = self.statistics.mode(data)
        self.assertEqual(3, result)

    def test_statistics_calculator_return_NoMode(self):
        data = [1, 2, 3, 4, 5]
        result = self.statistics.mode(data)
        self.assertEqual('no mode', result)
    # Test Mode -------------------------------------------------------------

    # Test Median -------------------------------------------------------------
    def test_statistics_calculator_return_median(self):
        data = [1, 2, 3, 4, 5, 6]
        result = self.statistics.median(data)
        self.assertEqual(3.5, result)

    def test_statistics_calculator_return_median2(self):
        data = [1, 2, 3, 4, 5]
        result = self.statistics.median(data)
        self.assertEqual(3, result)
    # Test Median -------------------------------------------------------------

    # Test Variance -------------------------------------------------------------
    def test_statistics_calculator_return_variance(self):
        data = [1, 2, 3, 4, 5, 6]
        result = self.statistics.variance(data)
        self.assertEqual(2.9166666666666665, result)

    # Test Standard Deviation -----------------------------------------------
    def test_statistics_calculator_return_stand_deviation(self):
        data = [1, 2, 3, 4, 5, 6]
        result = self.statistics.st_dev(data)
        self.assertEqual(1.8708286933869707, result)

    # Test Quartiles -----------------------------------------------
    def test_statistics_calculator_return_quartiles(self):
        data = [3,5,6]
        result = self.statistics.quartile(data,0.25,0,None)
        self.assertEqual(4, result)

    # Test Skew -----------------------------------------------
    def test_statistics_calculator_return_skew(self):
        data = [3, 5, 6, 5, 3, 2, 1, 40]
        result = self.statistics.skew(data,None,None)
        self.assertEqual(2.1923866091383113, result)



if __name__ == '__main__':
    unittest.main()
