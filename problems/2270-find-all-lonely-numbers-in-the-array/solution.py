from collections import defaultdict

class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
      counts = defaultdict(int)
      for num in nums: counts[num] += 1
      return [num for num in nums if counts[num] == 1 and counts[num+1] == 0 and counts[num-1] == 0]
