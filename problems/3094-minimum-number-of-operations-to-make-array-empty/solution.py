from collections import defaultdict

class Solution:
    def minOperations(self, nums: List[int]) -> int:
      counts = defaultdict(int)
      for num in nums: counts[num] += 1

      ans = 0
      for num in counts.values():
        if num < 2: return -1
        if num % 3 == 0: 
          ans += num // 3
          continue
        elif num % 3 == 1: 
          p = num % 2
          n = (num // 3) * 3
          if n%2 != p: n -= 3
          ans += n // 3
          num -= n
        elif num % 3 == 2: 
          ans += num // 3
          num = 2 
        if num % 2 == 0: ans += num // 2
        else: return -1
      return ans
