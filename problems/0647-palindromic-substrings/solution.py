class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = len(s)

        for l in range(2, len(s) + 1):
            for i in range(0, len(s) - l + 1):
                if s[i:i+l] == s[i:i+l][::-1]: ans += 1

        return ans
        
