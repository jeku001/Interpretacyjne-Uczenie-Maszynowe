import pandas as pd

class Analysis:
    def __init__(self):
        pass

    @staticmethod
    def loadData(filename):
        return pd.read_csv(filename)

    @staticmethod
    def findMissingValues(data):
        missing = data.isnull()
        total_missing = missing.sum().sum()

        if total_missing == 0:
            print("No missing values.")
        else:
            print("Columns with missing values:")
            print(data.isnull().sum()[data.isnull().sum() > 0])
            print("\nRows with missing values:")
            print(data[data.isnull().any(axis=1)])