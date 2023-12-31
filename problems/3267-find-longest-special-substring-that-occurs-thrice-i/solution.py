class Solution:
    def maximumLength(self, s: str) -> int:
        return self.solve(s)
    
    def getCount(self, s, ss):
        i, l = 0, len(s)
        ans = 0
        while i<l:
            if s[i:].startswith(ss): ans += 1
            i += 1
        return ans
    
    def solve(self, s):
        i, l, ans = 0, len(s), -1
        while i<l-2:
            cl = 1
            while i+cl-1<l and s[i+cl-1] == s[i]:
                ss = s[i:i+cl]
                if self.getCount(s, ss) >= 3: ans = max(ans, len(ss))
                cl += 1
            i += 1
        return ans
