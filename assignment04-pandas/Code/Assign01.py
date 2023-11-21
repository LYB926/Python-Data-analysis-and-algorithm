# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 17:38:23 2021

@author: Ziwei
"""

# TODO: 导入numpy库并简写为np
import numpy as np
# TODO: 导入Pandas库并简写为pd
import pandas as pd

# TODO: 通过列表生成式创建一维列表，元素为1,3,5, ...,21，从列表创建Series s1
s = [_ for _ in range(1, 22, 2)]
s1 = pd.Series(s)
print('Series s1 = \n', s1)

# TODO:从 NumPy 数组创建 DataFrame df1
# 1. 创建6行4列的0-1分布的随机数数组num_arr
# 2. 从num_arr创建dataframe对象df1，列索引为'A'、'B'、'C'、'D'，行索引为dates
num_arr = np.random.rand(6, 4)
df1 = pd.DataFrame(num_arr)
dates = pd.date_range('today', periods=6) # 定义时间序列作为index
print('df1 = \n', df1)

# TODO: 从无列标题的 ex1.csv中创建DataFrame对象df2，分隔符为“,”， 并设置列索引为'a','b','c','d','message'
df2 = pd.read_csv('ex1.csv', header=None, names=['a', 'b', 'c', 'd', 'message'], sep=',')
print('df2 = \n', df2)

# TODO: 将 df2 保存为 df2.json 文件
df2.to_json('df2.json')

# TODO: 将df2的第1行的b列和c列数据改为10，并输出df2
df2.loc[0, 'b'] = 10
df2.loc[0, 'c'] = 10
print('修改数据后的 df2 = \n', df2)

# TODO: 将df2按照'c'列的值降序排序，得到新的Dataframe,记为df3
df3 = df2.sort_values(by='c',ascending=False)
print('df3 = \n', df3)

# TODO: df3删除message列，结果记为df4
df4 = df3.drop(labels='message', axis=1)
print('df4 = \n', df4)

# TODO: df4的每个数字减去该行的平均值，结果记为df5
row_means = df4.mean(axis=1)
df5 = df4.sub(row_means, axis=0)
print('df5 = \n', df5)
