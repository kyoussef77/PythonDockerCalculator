import unittest

from Calculator.Calculator import Calculator;

class MyTestCase(unittest.TestCase):


    def test_calculator_return_sum(self):
        calculator = Calculator()
        result = calculator.Sum(1,2)
        self.assertEqual(3, result)

    def test_calculator_return_difference(self):
        calculator = Calculator()
        result = calculator.Difference(2,4)
        self.assertEqual(float(-2), float(result))

    def test_calculator_access_difference_result(self):
        calculator = Calculator()
        calculator.Difference(2, 4)
        self.assertEqual(float(-2), calculator.Result)

    def test_calculator_access_sum_result(self):
        calculator = Calculator()
        calculator.Sum(2, 4)
        self.assertEqual(6, calculator.Result)

    def test_multiple_calculators(self):
        calcualtor1 = Calculator()
        calcualtor2 = Calculator()
        calcualtor3 = Calculator()

        calcualtor3.Sum(calcualtor1.Sum(1,2),calcualtor2.Difference(3,4))
        self.assertEqual(2,calcualtor3.Result)


if __name__ == '__main__':
    unittest.main()