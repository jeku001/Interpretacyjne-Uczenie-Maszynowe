import pandas as pd
import matplotlib.pyplot as plt
import math

from analysis import Analysis

#data explanation
analyzer = Analysis()
data = analyzer.loadData('data/raw_data/zal_hausing.csv')
print(data.head().to_string())
analyzer.findMissingValues(data)
