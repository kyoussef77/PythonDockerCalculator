import unittest

from Calculator.Calculator import Calculator;
from MathOperations.addition import Addition;
from MathOperations.subtraction import Subtraction;

class MyTestCase(unittest.TestCase):


    def test_calculator_addition(self):

        result = Addition.sum(1,2)
        self.assertEqual(3, result)

    def test_calculator_subtraction(self):

        result = Subtraction.difference(2,4)
        self.assertEqual(float(-2), float(result))


if __name__ == '__main__':
    unittest.main()