class Solution:
    def secondHighest(self, s: str) -> int:
        nums = sorted(list(set([int(c) for c in s if c.isdigit()])), reverse=True)
        if len(nums) > 1: return nums[1]
        return -1
