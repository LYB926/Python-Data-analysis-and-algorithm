'''
2.	编写程序，实现处理鸢尾植物数据集，要求：
    a)	导入鸢尾植物数据集(iris.csv)，保存为dataframe对象
    b)	求出鸢尾属植物萼片长度的平均值、中位数和标准差，使用print函数输出
    c)	筛选具有sepal_length<5.0并且petal_length>1.5的iris数据行
    d)	在c)的基础上，根据sepal_length列对数据集进行排序，新的数据集保存为iris2.csv
    e)	在鸢尾属植物数据集中找到最常见的花瓣长度值，使用print函数输出
    f)	找到鸢尾属植物萼片长度的第5和第95百分位数，使用print函数输出
    petal花瓣   sepal萼片
'''
import pandas as pd

iris = pd.read_csv('iris.csv')

sl_avg = iris['sepal_length'].mean()
sl_mid = iris['sepal_length'].median()
sl_std = iris['sepal_length'].std()
print("萼片长度的平均值为：{:.2f}, 中位数为：{:.2f}, 标准差为：{:.2f}\n" .format(sl_avg, sl_mid, sl_std) )

filtered = iris[(iris['sepal_length'] < 5.0) & (iris['petal_length'] > 1.5)]
#print('sepal_length<5.0并且petal_length>1.5的iris数据行:')
#print(filtered)

sorted_iris = filtered.sort_values(by='sepal_length', ascending=False)
sorted_iris.to_csv('iris2.csv')
#print(sorted_iris)

pl_mode = iris['petal_length'].mode()
pl_mode_str = pl_mode.to_string(index=False).replace('\n', ', ')
print('最常见的花瓣长度值为: {}\n'.format(pl_mode_str))
#print(pl_mode_str)

sl_quan95 = iris['sepal_length'].quantile(0.95)
sl_quan05 = iris['sepal_length'].quantile(0.05)
print('萼片长度的第5和第95百分位数分别为: {:.1f}, {:.1f}'.format(sl_quan05, sl_quan95))