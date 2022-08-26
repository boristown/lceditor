from typing import *

###code begin###

#1. 两数之和
#https://leetcode.cn/problems/two-sum/
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        
        return []

###code end###

if __name__ == '__main__':
    funcname = dir(Solution)[-1]
    solu = Solution()
    func = getattr(solu,funcname)
    param_cnt = func.__code__.co_argcount-1
    with open("in.txt","r") as infile:
        lines = infile.readlines()
    sample_cnt = len(lines) // param_cnt
    ind = 0
    for _ in range(sample_cnt):
        params = []
        for _ in range(param_cnt):
            params.append(eval(lines[ind]))
            ind += 1
        ans = func(*params)
        print(ans)