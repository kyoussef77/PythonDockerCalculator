import unittest
from Statistics.statistics import Statistics

class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.statistics = Statistics()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.statistics, Statistics)

    def test_decorator_calculator(self):
        self.assertIsInstance(self.statistics, Statistics)

    def test_statistics_calculator_return_mean(self):
        data = [1,2,3,4,5]
        result = self.statistics.mean(data)
        self.assertEqual(3, result)

    def test_random_int_seed(self):
        testdata = self.statistics.Random_int_nums(1, 100, 5, 5)
        mean = self.statistics.mean(testdata)
        self.assertEqual(mean, 48.2)

    def test_random_int(self):
        testdata = self.statistics.Random_int_nums(1, 100, 5, None)
        mean = self.statistics.mean(testdata)
        self.assertEqual(mean, 48.2)

    def test_random_float_seed(self):
        testdata = self.statistics.Random_float_nums(1, 100, 5, 3)
        mean = self.statistics.mean(testdata)
        self.assertEqual(mean, 36.132556091996484)

    def test_random_float(self):
        testdata = self.statistics.Random_float_nums(1, 100, 5, None)
        mean = self.statistics.mean(testdata)
        self.assertEqual(mean, 48.2)



if __name__ == '__main__':
    unittest.main()