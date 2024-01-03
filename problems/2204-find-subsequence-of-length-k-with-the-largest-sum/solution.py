class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
      l, i, sort = len(nums), 0, sorted(enumerate(nums), key=lambda x: x[1])
      
      while l>k:
        remove = sort[i][0]
        nums[remove] = None
        i += 1
        l -= 1
      
      return [num for num in nums if num is not None]
