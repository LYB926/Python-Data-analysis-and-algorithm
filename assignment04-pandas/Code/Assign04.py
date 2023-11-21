'''
4.	数据合并：
    1、将“student.csv“和”score.csv”中的数据合并，连接键为学号，合并结果如下：
    2、将“student-02.csv“和”score.csv”中的数据合并，连接键为学号，且合并结果以学号为索引，合并结果如下：
'''
import pandas as pd

stu1 = pd.read_csv('student.csv')
stu2 = pd.read_csv('student-02.csv')
score = pd.read_csv('score.csv')

merge1 = pd.merge(stu1, score, on='stdID', how='left')
print(merge1, '\n')

merge2 = pd.merge(score, stu1, on='stdID', how='right').set_index('stdID')
print(merge2, '\n')