class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
      l = len(nums)
      if l< 2: return True
      a, b = nums[0], nums[l-1]
      if a == b: return all([a == n for n in nums])
      cond = nums[l-1] > nums[0]

      for i in range(0, l-1):
        if nums[i+1] == nums[i]: continue
        elif (nums[i+1] > nums[i]) != cond: return False
      return True
