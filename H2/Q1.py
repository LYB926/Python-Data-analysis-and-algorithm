# 1.创建一个类MyArray，自定义数组的乘法（考虑一些输入错误的情况），并设计一些实例进行测试。

class MyArray:
    def __init__(self, *args):
        if not args:
            self.array = []
        else:
            for _ in args:
                if isinstance(_, (int, float)):
                    print ('Type error: element type should be int or float')
                    return
            self.array = list(args)
    
    def __mul__(self, x):
        if isinstance(x, (int, float)):
            t = tuple([_*x for _ in self])
            return (MyArray(t))
        elif isinstance(x, MyArray):
            if len(self.array) == len(x.array):
                t = tuple([a*b for a in self.array for b in x.array])
                return (MyArray(t))
            else:
                print ('Inconsistent array length.')
                return
        else:
            print ('Type error: operand type should be int, float or MyArray.')
            return
        
x = MyArray(1, 2, -1, 3)
y = MyArray(4, 3, 2, 1)
z = x * y
            

            