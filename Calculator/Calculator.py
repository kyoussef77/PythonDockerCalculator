

class Calculator:
    result = 0

    def __init__(self):
        pass

    def addition(self, a, b):
        return float(a) + float(b)

    def division(self, a, b):
        return float(b) / float(a)

    def subtraction(self, a, b):
        a = float(a)
        b = float(b)
        c = b - a
        return c

    def multiply(self, a, b):
        return float(a) * float(b)

    def square_root(self, a):
        return float(a) ** 0.5

    def square(self, a):
        return float(a) * float(a)


