'''平均满载率实验'''
import numpy as np
import pandas as pd
import time

filename = r"D:\repo\PythonLearning\PandasLearning\AGG-20150407.csv"
data = pd.read_csv(filename)
print(data.head(5))
print(data.info())
