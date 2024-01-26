class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pos = {}
        for i, n in enumerate(nums):
            if n in pos: return [pos[n], i]
            pos[target-n] = i
