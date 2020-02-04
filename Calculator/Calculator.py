from MathOperations.addition import Addition;
from MathOperations.subtraction import Subtraction;

class Calculator:
    result = 0

    def __init__(self):
        pass

    def Sum(self, a, b):
        return Addition.sum(a,b);



    def Difference(self, a, b):
       return Subtraction.difference(a,b)



