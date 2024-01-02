class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
      n, ans, i = str(num), 0, 0
      l = len(n)
      while i+k-1<l:
        divisor = int(n[i:i+k])
        if divisor != 0 and num % divisor == 0: ans += 1
        i += 1
      return ans
