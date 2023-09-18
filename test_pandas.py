import numpy as np
import pandas as pd

data = pd.read_csv('./test_pandas.csv',header=0)
dataList = data.values.tolist()
dataDict = data.to_dict('index')
print(dataDict)
