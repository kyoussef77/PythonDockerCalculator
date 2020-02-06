import unittest

from MathOperations.addition import Addition;
from MathOperations.subtraction import Subtraction;
from MathOperations.multiplication import Multiplication;

class MyTestCase(unittest.TestCase):

    def test_MathOperations_Sum(self):
        self.assertEqual(3, Addition.sum(1, 2))

    def test_MathOperations_Subtraction(self):
        self.assertEqual(-1, Subtraction.difference(1, 2))

    def test_MathOperations_Sum_list(self):
        numlist = [1,2,3]
        self.assertEqual(6, Addition.sum(numlist))

    def test_MathOperation_Product(self):
        self.assertEqual(35, Multiplication.product(7, 5))

    def test_MathOperations_Product_list(self):
        numlist = [2, 3, 4]
        self.assertEqual(24, Multiplication.product(numlist))



if __name__ == '__main__':
    unittest.main()