# 2.使用列表生成式实现矩阵转置，编写函数并运行下面的实例：
# M = [1, 4, 9; 16, 25, 36; 49, 64, 81]

# 1  4  9
# 16 25 36
# 49 64 81

def transPos(_m):
    return  [[row[i] for row in _m]for i in range(3)]

M = [[1, 4, 9], [16, 25, 36], [49, 64, 81]]
print (transPos(M))