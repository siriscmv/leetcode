from collections import defaultdict

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
      counts = defaultdict(int)
      for num in nums: 
        if num != 0: counts[num] += 1
      return len(counts.keys())
        
