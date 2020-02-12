from MathOperations.addition import Addition
from MathOperations.division import Division


def mean(data):
    num_values = len(data)
    total = 0
    total = Addition.sum(data)
    return Division.quotient(total, num_values)
