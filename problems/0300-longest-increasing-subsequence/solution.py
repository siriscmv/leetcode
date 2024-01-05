class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
      l = len(nums)
      dp = [1] * l 
      for i in range(l-2, -1, -1):
        m = 0
        for j in range(i+1, l):
          if nums[i] < nums[j]: m = max(m, dp[j])
        dp[i] += m
      return max(dp)
