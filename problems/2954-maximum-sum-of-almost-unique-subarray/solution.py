class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
      return max([sum(nums[i:i+k]) for i in range(0, len(nums)-k+1) if len(set(nums[i:i+k])) >= m], default=0)
