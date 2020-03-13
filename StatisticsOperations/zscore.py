from Statistics import Statistics as statistics

class Zscore:

    @staticmethod
    def zscore(data):
        mean = statistics.mean(data)
        stD = statistics.st_dev(data)
        for i in data:
            zscore = (i - mean) / stD
            return zscore
