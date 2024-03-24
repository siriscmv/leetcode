class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {"I":1, "V":5, "X":10, "L":50 ,"C":100, "D":500, "M":1000}
        ans = 0

        for i in range(len(s)-1):
            a, b = roman[s[i]], roman[s[i+1]]
            if a < b: ans -= a
            else: ans += a

        return ans + roman[s[-1]]
