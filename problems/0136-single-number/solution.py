from functools import reduce

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        return reduce(lambda x, y: x^y, nums, 0)
