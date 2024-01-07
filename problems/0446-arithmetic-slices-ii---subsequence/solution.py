from collections import defaultdict
from math import comb

class Solution:
    def edge_case(self, n) -> int:
      return sum([comb(n, k) for k in range(3, n+1)])

    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
      if len(set(nums)) == 1: return self.edge_case(len(nums))

      ln, cache, ans = len(nums), defaultdict(list), 0
      revmap = defaultdict(list)
      for i, num in enumerate(nums): revmap[num].append(i)
      for l in range(1, ln + 1):
        if l == 1: 
          for i in range(0, ln): cache[l].append((i,))
          continue
      
        for prev in cache[l-1]:
          li, lv = prev[-1], nums[prev[-1]]
          diff = lv-nums[prev[-2]] if l>=3 else 0
          
          if l == 2: 
            for j in range(li+1, ln): cache[l].append(prev + (j,))
            continue
          
          for j in revmap[diff+lv]:
            if j <= li: continue
            cache[l].append(prev + (j,))
            ans += 1
        
        del cache[l-1]
      return ans
