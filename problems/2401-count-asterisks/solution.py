class Solution:
    def countAsterisks(self, s: str) -> int:
      skip, ans = False, 0
      for char in s:
        if char == '|': skip = not skip
        if not skip and char == '*': ans += 1
      return ans
