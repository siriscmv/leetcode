class Solution:
    dp={}
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        global dp
        dp={}
        return self.solve(n, k, target) % (10**9 + 7)

    def solve(self, n, k, target):
        global dp
        key = (n, k, target)
        if key in dp: return dp[key]

        s=0
        if n == 1:
            if target > 0 and target <= k: s+=1
            return s
        
        t = min(target, k)
        for i in range(1, t+1): s+= self.solve(n-1, k, target-i)
        
        dp[key] = s
        return s
