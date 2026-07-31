import statistics

class Dataset:
    def __init__(self, name, data):
        self.name = name
        self.data = data  # Assumed to be a list of numbers

    def mean(self):
        return statistics.mean(self.data)

    def median(self):
        return statistics.median(self.data)

    def std(self):
        return statistics.stdev(self.data)

    def summary(self):
        print(f"Dataset: {self.name}")
        print(f"Mean: {self.mean()}")
        print(f"Median: {self.median()}")
        print(f"Std Dev: {self.std()}")
