from lclibs import *
import lceditor

# Problem description:
'''

'''

###Solution begin###

# 1. 两数之和
# https://leetcode.cn/problems/two-sum/
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []

###Solution end###

if __name__ == '__main__':
    lceditor.run("sample1.txt")