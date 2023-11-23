'''
2.	给定下面的无向连通图顶点着色，有m=3种颜色可选，同一条边的两个顶点颜色不同。
要求创建如下图所示的图对象，并实现上色的函数，以列表形式返回所有可行的着色方案并打印出来。
'''
def check(t: int):
    for _ in range(1, t):
        if (graph[t][_] == 1 and color[t] == color[_]):
            return False
    return True

# 回溯+dfs
def back(c: int):
    global nums, ans
    if (c > N):
        nums = nums + 1
        print('{}: '.format(nums), end='')
        for _ in range(1, N+1):
            print('{}'.format(color[_]), end='')
        print('\n', end='')
        ans.append(color[1:N+1])
    else:
        for i in range(1, M+1):
            color[c] = i
            if (check(c)==True):
                back(c+1)
            color[c] = 0
    return ans

# 输入颜色数量、图节点数量和所有的连接，“23”表示2-3存在连接
M = int(input('Available colors = '))
N = int(input('Graph size = '))
connects = []
print('Input all graph connects: ')
while True:
    try:
        connects.append(input())
    except:
        break

# 使用邻接矩阵的方式构造图
nums = 0
ans = [] 
color = [0 for _ in range(N+1)]
graph = [[0 for _ in range(N+1)] for _ in range(N+1)]
for _ in connects:
    graph[int(_[0])][int(_[1])] = 1
    graph[int(_[1])][int(_[0])] = 1
ans = back(1)
print('以上是所有{}种可行方式'.format(nums))