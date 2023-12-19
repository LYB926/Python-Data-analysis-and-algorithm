'''
4.	给定一个包含N个不等元素的数组，输出其中位数。要求采用O(NlogN)复杂度的算法实现。要求测试下例：
（1）[4,10,3,7,5,2]
（2）[8,2,3,5,7,6,11,14,1,9,13,10,4,12,15]
'''
# 快速排序时间复杂度：O(NlogN)
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
    
#arr = [4,10,3,7,5,2]
arr = [8,2,3,5,7,6,11,14,1,9,13,10,4,12,15]

arr_sorted = quick_sort(arr)
median = arr_sorted[int(len(arr_sorted)/2)]
print('array = {}'.format(arr))
print('中位数为： {}'.format(median))