class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
      ans = ''
      for i, d in enumerate(number):
        if digit != d: continue
        ans = max(ans, number[:i] + number[i+1:])
      return ans
