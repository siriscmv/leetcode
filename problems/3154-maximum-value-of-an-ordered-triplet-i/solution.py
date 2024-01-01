class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
      ans = 0
      for i in range(0, len(nums)-2):
        for j in range(i+1, len(nums)-1):
          diff = nums[i] - nums[j]
          ans = max(ans, diff * max(nums[j+1:]))
      return ans
