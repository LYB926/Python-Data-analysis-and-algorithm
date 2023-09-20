# 3.函数递归解决汉诺塔问题：有A、B、C三根柱子，A上从小到大叠有n个圆盘，要求将A的圆盘移到C，一次只能移一个盘子且大盘子不能在小盘子上面。
# 编写函数move(n, A, B, C)，要求打印出每一步移动盘子的操作（如，A --> C），并运行实例move(4,'A','B','C')。

def move(n, A, B, C):
    if n == 1:
        print(A, '-->', C)
    else:
        move(n - 1, A, C, B)
        print(A, '-->', C)
        move(n - 1, B, A, C)

move (4,'A','B','C')