# -*- coding:utf-8 -*-
# 鸢尾花数据集
from sklearn.datasets import load_iris
iris_dataset =load_iris() # 加载数据 里面的数据和字典很相似 k-v
"""
print("Keys:\n{}".format(iris_dataset.keys()))
# dict_keys(['data', 'target', 'target_names', 'DESCR', 'feature_names'])
print(iris_dataset['DESCR']) # description
print(iris_dataset['target_names']) # ['setosa' 'versicolor' 'virginica'] 具体分类名称(结果)
print(iris_dataset['feature_names']) # ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)'] 属性名称
# print(iris_dataset['data']) # 花萼长 宽  花瓣长 宽
print( iris_dataset['data'][:5]) #(150, 4) 行列
print( iris_dataset['target'].shape) # 表示结果 0 1 2
print(iris_dataset)
"""
# 测试数据和 训练数据
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(
    iris_dataset['data'],iris_dataset['target'],random_state=1
)
# print(X_train,X_test,X_train.shape)
#  .................
#  [5.9 3.  5.1 1.8]
#  [6.8 3.  5.5 2.1]
#  [4.3 3.  1.1 0.1]
#  [4.8 3.  1.4 0.1]
#  [6.  2.9 4.5 1.5]
#  [5.8 2.7 5.1 1.9]] (112, 4) 每次结果不同
# 利用X_train 中的数据创建DataFrame
# 利用不同的feature_names中的字符串对数据列进行标记
import pandas as pd
import mglearn
import operator
from functools import reduce

iris_dataframe = pd.DataFrame(X_train,columns=iris_dataset.feature_names)
# 利用DataFrame 创建三点矩阵图 按y_train 着色
grr = pd.plotting.scatter_matrix(iris_dataframe,c=y_train,figsize=(15,15),marker='o',hist_kwds={'bins':20},s=60,alpha=.8,cmap=mglearn.cm3)

