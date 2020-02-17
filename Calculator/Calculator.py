from MathOperations.addition import Addition;
from MathOperations.subtraction import Subtraction;
from MathOperations.multiplication import Multiplication;
from MathOperations.division import Division;
from MathOperations.exponentiation import Exponentiation;
from MathOperations.nthRoot import NthRoot;

from MathOperations.random import Random_num;

class Calculator:
    Result = 0

    def __init__(self):
        pass

    def Sum(self, a, b):
        self.Result = Addition.sum(a, b)
        return self.Result

    def Difference(self, a, b):
        self.Result = Subtraction.difference(a, b)
        return self.Result

    def Product(self, a, b):
        self.Result = Multiplication.product(a, b)
        return self.Result

    def Quotient(self, a, b):
        self.Result = Division.quotient(a, b)
        return self.Result

    def Power(self, a, b):
        self.Result = Exponentiation.power(a, b)
        return self.Result

    def Root(self, a, b):
        self.Result = NthRoot.root(a, b)
        return self.Result



