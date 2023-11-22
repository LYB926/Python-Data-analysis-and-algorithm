'''
3.	数据合并：输入一个其中元素值各不相同的整数数组和一个目标整数，返回所有可能的数组元素的组合，使得其和等于目标值。
测试例如下：
输入: candidates = [2,3,5], target = 8
输出：[[2,2,2,2],[2,3,3],[3,5]] 
'''
def search(index: int, sum: int, nums: list[int], target: int):
    global ans, path
    if (sum == target):
        ans.append(path[:])
        return
    for _ in range(index, len(nums)):
        sum = sum + nums[_]
        if (sum <= target):
            path.append(nums[_])
            search(_, sum, nums, target)
            path.pop()
            sum = sum - nums[_]
        else:
            return

nums_str, target_str = input('candidates = '), input('target = ')
nums = [int(_) for _ in nums_str if (_.isnumeric()==True)]
target = int(target_str)
ans, path = [], []
search(0, 0, nums, target)
print(ans)