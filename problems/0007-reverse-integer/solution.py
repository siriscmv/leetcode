class Solution:
    def reverse(self, x: int) -> int:
      n = 0
      while x:
        n = n*10 + x % (10 if x>0 else -10)
        x = int(x / 10)
      
      return n if -1 * 2**31 <= n <= 2**31-1 else 0
