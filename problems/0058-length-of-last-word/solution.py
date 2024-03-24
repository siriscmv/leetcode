class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        seen, n = 0, len(s)

        for i in range(n - 1, -1, -1):
            if s[i] == " ": 
                if seen: return seen - i
            elif not seen: seen = i
        
        return seen + 1
