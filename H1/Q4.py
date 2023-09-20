# 4.编写一个str2float()函数，利用map()和reduce()
# 把输入字符串转换成浮点数，例如'123.456’ →123.456。

from functools import reduce
def f(x, y):
    return x * 10 + y

def str2float(s):
    pointPos = s.index('.')
    s1 = list(map(int, [x for x in s[: pointPos]]))
    s2 = list(map(int, [x for x in s[pointPos + 1:]]))
    return reduce(f, s1) + reduce(f, s2) / 10 ** len(s2)

str = '123.456'
num = str2float(str)
print(num,'\n', type(num))