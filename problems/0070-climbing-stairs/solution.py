class Solution:
    def __init__(self):
        self.dp = [0, 1, 2]

    def climbStairs(self, n: int) -> int:
        for i in range(len(self.dp), n+1): self.dp.append(self.dp[-1] + self.dp[-2])
        return self.dp[n]
