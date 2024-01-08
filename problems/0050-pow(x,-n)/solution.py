class Solution:
    dp = {}
    def myPow(self, x: float, n: int) -> float:
      global dp
      dp = {}
      return self.solve(x, n)
    
    def solve(self, x, n):
      global dp
      if n in dp: return dp[n]
      if n == 0: return 1
      if n == 1: return x
      if n == -1: return 1/x

      a, b = self.myPow(x, n // 2), self.myPow(x, n % 2)
      dp[n] = a * a * b
      return dp[n]
