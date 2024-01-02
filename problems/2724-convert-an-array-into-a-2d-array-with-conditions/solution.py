from collections import defaultdict

class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
      counts, m = defaultdict(int), 0
      for num in nums: 
        counts[num] += 1
        m = max(m, counts[num])
      
      grid = [[] for _ in range(m)]
      for ch in counts:
        cnt = counts[ch]
        for i in range(0, cnt): grid[i].append(ch)
      
      return grid
