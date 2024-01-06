class Solution:
    def partitionString(self, s: str) -> int:
        ans, seen = 0, set()
        if not s: return 0
        for char in s:
          if char in seen: 
            ans += 1
            seen.clear()
          seen.add(char)
        return ans+1
