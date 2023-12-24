import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize']=(6, 6)
# 用于解决N皇后问题的类
class NQueen:
    # 初始化
    def __init__(self) -> None:
        self.ans = []
        self.ansNum = -1  # 将解的数量初始化为-1，方便后续进行异常处理
        
    # solver函数用于计算N皇后问题的所有解
    def solver(self, N: int):
        # 记录结果和皇后所在列的数组
        ans = [] 
        col = [0] * N
        # 使用三个数组标记当前列和两条对角线的冲突情况，以便进行DFS减枝
        vertical = [False] * N
        diagonal1, diagonal2 = [False] * (N*2-1), [False] * (N*2-1)
        # 使用深度优先搜索（DFS）求解
        def dfs(row):
            # row = N，所有的行都已经放置了皇后
            if (row == N):
                ans.append(col[:])
            # 还未放置完，继续递归求解
            for c, on in enumerate(vertical):
                # 判断第c列是否可以放置
                if ((not on)and(not diagonal1[row + c])and(not diagonal2[row - c])):
                    col[row] = c
                    # 更新当前列和两条对角线的冲突情况
                    vertical[c] = diagonal1[row + c] = diagonal2[row - c] = True
                    dfs(row + 1)
                    vertical[c] = diagonal1[row + c] = diagonal2[row - c] = False

        dfs(0)
        self.ans = ans
        self.ansNum = len(ans)
        return ans

    # draw(n)函数用于在求出解后，绘制出八皇后问题的第n个解法
    def draw(self, n: int) -> None:
        # if (len(self.ans) == 0):
        #     print("NO solution.")
        # if ((n < 0)or(n >= len(self.ans))):
        #     print("Invalid solution index.")
        #     return

        fig, ax = plt.subplots()
        # 使用Matplotlib绘制棋盘
        for i in range(len(self.ans[n])+1):
            plt.plot([i, i], [0, len(self.ans[n])], color='black')
            plt.plot([0, len(self.ans[n])], [i, i], color='black')

        # 标出皇后的位置
        for i, col in enumerate(self.ans[n]):
            plt.scatter(col + 0.5, len(self.ans[n]) - i - 0.5, marker='^', color='red', edgecolors='black', s=75)
        
        # 保存绘制出的结果
        plt.axis('off')
        fig.set_size_inches(2, 2)
        plt.tight_layout()
        plt.savefig('solution_image.png', dpi=75)
        # plt.show()
        plt.close()
