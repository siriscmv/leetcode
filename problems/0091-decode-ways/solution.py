class Solution:
    def numDecodings(self, s: str) -> int:
        if (s[0] == '0'): return 0
        i=len(s)-1
        dp = {}
        dp[i] = 1 if s[i] != '0' else 0
        dp[i+1] = 1
        i-=1

        while i>=0:
            if s[i] != '0': dp[i] = dp[i+1]
            else: dp[i] = 0
            if s[i] != '0' and int(s[i:i+2])<=26: dp[i] += dp[i+2]
            i-=1
        
        return dp[0]
