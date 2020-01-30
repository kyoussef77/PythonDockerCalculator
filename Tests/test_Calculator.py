import unittest

from Calculator.Calculator import Calculator;

class MyTestCase(unittest.TestCase):

    def test_instantiate_calculator(self):
        calculator = Calculator()
        self.assertIsInstance(calculator, Calculator)

    def test_calculator_addition(self):
        calculator = Calculator()
        result = calculator.addition(1,2)
        self.assertEqual(3, result)

    def test_calculator_subtraction(self):
        calculator = Calculator()
        result = calculator.subtraction(2,4)
        self.assertEqual(float(2), float(result))

    def test_calculator_multiplication(self):
        calculator = Calculator()
        result = calculator.multiply(4,5)
        self.assertEqual(float(20), float(result))

    def test_calculator_square_root(self):
        calculator = Calculator()
        result = calculator.square_root(9)
        self.assertEqual(float(3), float(result))

    def test_calculator_square(self):
        calculator = Calculator()
        result = calculator.square(9)
        self.assertEqual(float(81), float(result))
if __name__ == '__main__':
    unittest.main()