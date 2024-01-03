class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        needed = set()
        for i in range(1, k+1): needed.add(i)

        i, l = 0, len(nums)-1
        while l-i >= 0:
          needed -= { nums[l-i] }
          i += 1
          if not needed: return i
