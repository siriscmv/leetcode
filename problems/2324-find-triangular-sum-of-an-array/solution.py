class Solution:
    def triangularSum(self, nums: List[int]) -> int:
      l = len(nums)
      if l == 1: return nums[0]
      for i in range(l-1): nums[i] = (nums[i] + nums[i+1]) % 10
      del nums[l-1]
      return self.triangularSum(nums)
