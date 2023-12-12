'''	
最优装载问题：n个集装箱装船，集装箱重量为w_i，轮船载重为C。计算使得上船的集装箱数量最大的数量，并分析算法复杂度。
要求测试下例：
（1）W = [3,9,8,1,2,5,7], C = 12
（2）W = [3,7,8,6,5,3,4,3], C = 20
'''

def quick_sort(arr):
    if len(arr) >= 2:
        key = arr[len(arr)//2] 
        right, left = [], []  
        arr.remove(key)  

        for i in arr:
            if i < key:
                left.append(i)
            else:
                right.append(i)
        return quick_sort(left)+[key]+quick_sort(right)
    else:
        return arr
    
#W = [3,9,8,1,2,5,7]
#C = 12
W = [3,7,8,6,5,3,4,3]
C = 20
print('W = ', W, '\nC = ', C, '\n集装箱装载顺序为：')
w_sorted = quick_sort(W)

for _ in w_sorted:
    if (C - _ >= 0):
        C = C - _
        print('{}'.format(_), end='  ')
    else:
        break
