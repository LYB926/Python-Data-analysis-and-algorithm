# 1.创建一个类MyArray，自定义数组的乘法（考虑一些输入错误的情况），并设计一些实例进行测试。

class MyArray:
    def __init__(self, *args):
        if not args:
            self.array = []
        else:
            for _ in args:
                if not isinstance(_, (int, float)): # 检查数组元素类型是否合法
                    print ('Type error: element type should be int or float')
                    return
            self.array = list(args)
            print(self)
       
    def __str__(self):
        return str(self.array)
    __repr__ = __str__

    # 运算符重载
    def __mul__(self, x):
        if isinstance(x, (int, float)): # 数乘的情况
            t = [_*x for _ in self.array]
            v = MyArray()
            v.array = t
            return (v)
        elif isinstance(x, MyArray):    # 数组相乘的情况
            if len(self.array) == len(x.array):
                t = [a*b for a,b in zip(self.array, x.array)]
                v = MyArray()
                v.array = t
                return (v)
            else:                       # 检查输入数组长度是否相等
                print ('Inconsistent array length.')
                return
        else:                           # 考虑操作数是否合法
            print ('Type error: operand type should be int, float or MyArray.')
            return

# 功能测试部分代码
print('数组声明：')
x = MyArray(1, 2, -1, 3)
y = MyArray(4, 3, 2, 1)
z = MyArray(2, 5, 8)
r = MyArray(7, 2, 'z')
print('\n数组运算：')
print(x * 5)
print(x * y)
print(x * z)
print(x * 'x')

            