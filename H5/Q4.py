"""
4.	给定一个MxN的网格，其中0表示可行位置，-1表示障碍物。从指定起点出发到指定终点位置，你可以沿着上下左右四个方向前进。返回所有可能的路径（注：每个可行位置最多只能经过一次）。
测试例：
输入: grid = [[0,0,0,-1],[0,-1,0,0],[0,0,0,0]], src=(0,0), des=(2,2)
输出: 3 possible paths

"""

def dfs(x, y):
    global num
    for i in range(0, 4):
        dir = [(-1, 0), (0, -1), (1, 0), (0, 1)]  
        nx, ny = x + dir[i][0], y + dir[i][1]
        if nx < 0 or nx >= hx or ny < 0 or ny >= wy: 
            continue
        if [nx, ny] == dst:
            num += 1
            continue  
        if grid[nx][ny] == 0:
            grid[nx][ny] = 1
            dfs(nx, ny)

grid, src, dst = [], [], []      
grid_str, src_str, dst_str = input('grid = ').split('],['), input('src = '), input('des = ')
for i in range(len(grid_str)):
    tmp = []
    for j in grid_str[i]:
        if (j.isnumeric() == True):
            tmp.append(int(j))
    grid.append(tmp)
src = [int(_) for _ in src_str if(_.isnumeric()==True)]
dst = [int(_) for _ in dst_str if(_.isnumeric()==True)]

num = 0
wy, hx = len(grid[0]), len(grid)
dfs(src[0], src[1])  

print ('{} possible paths'.format(num))
