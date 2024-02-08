class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        for i in range(1, n + 1):
            mn = float('inf')
            j = 1
            while j ** 2 <= i:
                mn = min(mn, dp[i - j * j] + 1)
                j += 1
            dp[i] = mn
        return dp[n]
