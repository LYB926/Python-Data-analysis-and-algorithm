'''
3.	数据规整：对于2012欧洲杯球队数据Euro2012_stats.csv进行操作：
    1、	读入数据，命名为soccer，输出
    2、	根据进球数（Goals）从高到低排序，输出排序后结果
    3、	将红牌（Red Cards）列的缺失值填充为0，并统计黄牌和红牌各自的总数，输出
'''
import pandas as pd

soccer = pd.read_csv('Euro2012_stats.csv')
print('soccer = \n', soccer, '\n')

soccer_sorted = soccer.sort_values(by='Goals', ascending=False)
print('按进球数排序后的数据：\n', soccer_sorted, '\n')

soccer.fillna(value={'Red Cards': 0}, inplace=True)
print('填充红牌数中缺失值为0后的数据：\n', soccer, '\n')
total_red = soccer['Red Cards'].sum()
total_yellow = soccer['Yellow Cards'].sum()
print('总黄牌数和红牌数为: {}, {}'.format(total_red, total_yellow))