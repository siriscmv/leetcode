class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
      prefix, suffix = [], []

      seen = set()
      for num in nums:
        seen.add(num)
        prefix.append(len(seen))

      seen = set()
      for num in reversed(nums):
        suffix.append(len(seen))
        seen.add(num)
      suffix = suffix[::-1] + [0]

      ans = []
      for i in range(len(nums)): ans.append(prefix[i] - suffix[i])
      return ans
