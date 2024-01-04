class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
      ln = len(nums)
      if ln == 0: return 0
      l, r = 0, sum(nums)-nums[0]
      for i, num in enumerate(nums):
        if l == r: return i
        l += num
        r -= nums[i+1] if i+1<ln else 0
      return -1
