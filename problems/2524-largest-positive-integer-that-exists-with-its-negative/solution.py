class Solution:
    def findMaxK(self, nums: List[int]) -> int:
      nums.sort()
      start, end = 0, len(nums) - 1

      while nums[start] < 0 and nums[end] > 0 and start < end:
        if nums[end] == -1 * nums[start]: return nums[end]
        if -1 * nums[start] > nums[end]: start += 1
        else: end -= 1
      return -1
