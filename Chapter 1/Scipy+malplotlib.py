# -*- coding:utf-8 -*-
import numpy
from scipy import sparse
tu = [
        [1,7,0,0],
        [0,2,8,0],
        [5,0,3,9],
        [0,6,0,4],
    ]
x = numpy.array(tu)
# 生成 矩阵
E = numpy.eye(4)
# 稀疏矩阵
sparse_matrix = sparse.csr_matrix(tu)
# print("CSR 格式:\n{}".format(sparse_matrix))
# print("COO 格式:\n{}".format(sparse.coo_matrix(sparse_matrix)))
# 全部都是标准 行列格式？？

import matplotlib.pyplot as plt
# 在 -10 和10之间生成一个数列 共100个
xzhou = numpy.linspace(-10,10,100)
# 用正弦函数创建第二个数组
yzhou = numpy.sin(xzhou)
# 绘图
plt.plot(xzhou,yzhou,marker = '*')
plt.show()
