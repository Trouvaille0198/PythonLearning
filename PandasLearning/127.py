# %%
import numpy as np
import pandas as pd
import time


def cut(data):
    position = data.find(' ')
    data2 = data[:position]+' 00:00:00'
    result = time.mktime(time.strptime(data, "%Y-%m-%d %H:%M:%S")) - \
        time.mktime(time.strptime(data2, "%Y-%m-%d %H:%M:%S"))
    return result


filename = r"D:\repo\PythonLearning\PandasLearning\transfer.csv"
data = pd.read_csv(filename)
print(data.head(5))
print(data.info())

data["transfered_inTime"] = data["inTime"].apply(
    lambda x: cut(x))
data["transfered_outTime"] = data["outTime"].apply(
    lambda x: cut(x))


data['inTime'] = pd.to_datetime(data['inTime'])
data['outTime'] = pd.to_datetime(data['outTime'])
data['dayName'] = data['inTime'].dt.dayofweek
data['dayName'] = data['outTime'].dt.dayofweek
print(data.head(5))
print(data.info())

# data.to_csv(r"D:\repo\PythonLearning\PandasLearning\result.csv")
