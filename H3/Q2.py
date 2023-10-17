# 2. 编写程序，实现批量模拟5000次随机漫步
import numpy as np

# a. 每次随机漫步：从0开始，等概率步进1或-1，走1000步
#    编写一次随机漫步的程序，返回向一个方向累积行走的最远距离和是否偏离中心0点累积超过30
def randomWalk():
    direction = np.random.choice([-1,1], size=1000, p=[0.5,0.5])
    pos = direction[0]
    maxLen = 0
    tmpLen = 0
    above30 = False
    i = 1
    while i<1000:
        pos = pos+direction[i]
        if (pos > 30 or pos < -30):
            above30 = True
        if (direction[i]==direction[i-1]):
            tmpLen = tmpLen + 1
            if (tmpLen > maxLen):
                maxLen = tmpLen
        else:
            tmpLen = 0
        i = i + 1
    return maxLen+1, above30

# b. 统计5000次仿真中，向一个方向累积行走的最远距离
# c. 统计5000次仿真中，偏离中心0点累积超过30的次数
maxLen = 0
n = 0
for _ in range(0, 1000):
    m, a = randomWalk()
    if (m > maxLen):
        maxLen = m
    if (a == True):
        n = n + 1

print('向一个方向累积行走的最远距离: %d\n偏离中心0点累积超过30的次数: %d\n'  %(maxLen, n))


