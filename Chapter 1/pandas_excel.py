# -*- coding:utf-8 -*-
import pandas as pd
from IPython.display import display
data = {
    "Name":["John","Peter","Linda","Tom"],
    "Age":[24,2,55,22],
    "Location":["New York","Paris","Beijing","London"]
}
data_pandas = pd.DataFrame(data)
display(data_pandas)
# 选择年龄大于23的
display(data_pandas[data_pandas.Age>30])
