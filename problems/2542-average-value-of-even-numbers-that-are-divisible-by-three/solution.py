class Solution:
    def averageValue(self, nums: List[int]) -> int:
      ans = [n for n in nums if n%6 == 0]
      if not ans: return 0
      return sum(ans) // len(ans)
        
