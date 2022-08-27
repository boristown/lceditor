from lclibs import *
import lceditor
###code begin###

# 303. 区域和检索 - 数组不可变
# https://leetcode.cn/problems/range-sum-query-immutable/
class NumArray:

    def __init__(self, nums: List[int]):
        self.sums = [0]
        _sums = self.sums

        for num in nums:
            _sums.append(_sums[-1] + num)

    def sumRange(self, i: int, j: int) -> int:
        _sums = self.sums
        return _sums[j + 1] - _sums[i]

###code end###

if __name__ == '__main__':
    lceditor.run("sample2.txt")