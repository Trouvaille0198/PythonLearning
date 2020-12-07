# %%
import numpy as np
import pandas as pd

filename = r"D:\repo\PythonLearning\PandasLearning\data.csv"
data = pd.read_csv(filename)
a = [x for x in range(0, 145)]
data.columns = a
print(data.head(5))
print(data.info())

df1 = pd.DataFrame(np.zeros((313, 145), dtype=np.int16))
print(df1)
plus = 2
for i in range(0, 313):
    for j in range(1, 145):
        df1.iloc[i, 0] = str(i+111)
        df1.iloc[i, j] = int(data.iloc[i+plus, j]) + \
            int(data.iloc[i+plus+1, j])
    plus += 1
print(df1.head(5))
df1.to_csv("result.csv")
