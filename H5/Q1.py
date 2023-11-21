'''
1.	给定一个由 ‘1’（陆地）和 ‘0’（水）组成的二维网格，上下左右相连的全1区域视为一个岛屿，计算网格中岛屿的最大面积。
'''
# 对grid进行DFS搜索的函数
# depth用于记录DFS搜索的深度，即岛屿的面积
def dfs(x, y):
    global grid, depth
    depth = depth + 1
    grid[x][y] = 0
    for _ in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
        _x, _y = x + _[0], y + _[1]
        if (0 <= _x < row and 0 <= _y < col and grid[_x][_y] == '1'):
            dfs(_x, _y)

# 从控制台读取多行数组输入
grid, grid_str = [], []
while True:
    try:
        grid_str.append(input())
    except:
        break
for i in range(1, len(grid_str)):
    grid_row = []
    for j in grid_str[i]:
        if(j=='0' or j=='1'):
            grid_row.append(j)
    grid.append(grid_row)

# 对每个岛屿进行DFS，同时记录最大面积
max_depth = 0
row, col = len(grid), len(grid[0])
for i in range(row):
    for j in range(col):
        if (grid[i][j] == '1'):
            depth = 0
            dfs(i, j)
            max_depth = depth if (depth > max_depth) else max_depth
# 打印结果
print(max_depth)