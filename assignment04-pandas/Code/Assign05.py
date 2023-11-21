#5.	读取文件flightData.txt，根据舱位值为分组，通过绘制箱线图统计各组飞行时间，绘图需要标注标题、XY轴标签

import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams["font.sans-serif"]=["SimHei"]

flight = pd.read_table('flightData.txt')
boxplot = flight.boxplot(column='飞行时间', by='舱位')
boxplot.set_title("不同舱位的飞行时间箱线图")
boxplot.set_xlabel('舱位')
boxplot.set_ylabel('飞行时间 (h)')
plt.suptitle('')
plt.show()