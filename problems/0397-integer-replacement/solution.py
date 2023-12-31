class Solution:
    dp={}
    def integerReplacement(self, n: int) -> int:
        global dp
        dp={}
        return self.solve(n)
    
    def solve(self, n: int) -> int:
        global dp
        key = n
        if key in dp: return dp[key]
        c = 0
        while n%2 == 0: 
            n //= 2
            c += 1

        if n == 1: 
            dp[key] = c
            return c
        dp[key] = c + 1 + min(self.solve(n-1), self.solve(n+1)) 
        return dp[key]  
