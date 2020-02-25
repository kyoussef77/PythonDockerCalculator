import unittest
from numpy.random import seed
from numpy.random import randint
from Calculator.Calculator import Calculator
from Statistics.Statistics import Statistics


class MyTestCase(unittest.TestCase):
    # setUp is run before anything else so this is where you put things you want repeated or done in multiple methods
    # setUp --> test
    def setUp(self):
        self.calculator = Calculator()
        self.statistics = Statistics()

    def test_calculator_return_sum(self):
        result = self.calculator.Sum(1, 2)
        self.assertEqual(3, result)

    def test_calculator_return_difference(self):
        result = self.calculator.Difference(2, 4)
        self.assertEqual(float(-2), float(result))

    def test_calculator_return_Product(self):
        result = self.calculator.Product(2, 4)
        self.assertEqual(8, float(result))

    def test_calculator_return_Quotient(self):
        result = self.calculator.Quotient(2, 4)
        self.assertEqual(0.5, result)

    def test_calculator_return_Power(self):
        result = self.calculator.Power(4, 5)
        self.assertEqual(1024, result)

    # data is stored in the calculator object in "Result"
    def test_calculator_access_difference_result(self):
        self.calculator.Difference(2, 4)
        self.assertEqual(float(-2), self.calculator.Result)

    def test_calculator_access_sum_result(self):
        self.calculator.Sum(2, 4)
        self.assertEqual(6, self.calculator.Result)

    def test_calculator_access_product_result(self):
        self.calculator.Product(2, 4)
        self.assertEqual(8, self.calculator.Result)

    def test_calculator_access_quotient_result(self):
        self.calculator.Quotient(5, 2.5)
        self.assertEqual(2, self.calculator.Result)

    def test_calculator_access_power_result(self):
        self.calculator.Power(0, 1)
        self.assertEqual(0, self.calculator.Result)






    def test_multiple_calculators(self):
        calculator1 = Calculator()
        calculator2 = Calculator()
        calculator3 = Calculator()

        self.calculator.Sum(calculator1.Sum(1, 2), calculator2.Difference(3, 4))
        self.assertEqual(2, self.calculator.Result)


if __name__ == '__main__':
    unittest.main()
