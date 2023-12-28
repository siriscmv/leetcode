class Solution:
    def countSegments(self, s: str) -> int:
        ans, prev, seen = 0, None, False
        for char in s:
            if seen and char == " " and prev != " ": ans += 1
            if not seen and char != " ": seen = True
            prev = char
        if not seen: return 0
        if prev != " ": ans += 1
        return ans
        
