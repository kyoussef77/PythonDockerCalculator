from numpy import quantile

class Quantile:
    @staticmethod
    def quartile(data,q,axis,kdims = False):
        return quantile(data,q,axis,kdims)