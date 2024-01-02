from collections import defaultdict

class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
      LEN = 2
      seen = defaultdict(int)
      for ch in words: seen[ch] += 1
      
      ans, plusOne = 0, False
      keys = list(set([''.join(sorted(k)) for k in seen.keys()]))
      
      for s in keys:
        if s[0] == s[1]:
          if seen[s] % 2 == 1: 
            plusOne = True
            ans += LEN * (seen[s] - 1)
          else: ans += LEN * seen[s]
        else:
          rev = s[::-1]
          val = min(seen[s], seen[rev])
          ans += LEN * val * 2
      
      if plusOne: ans += LEN
      return ans
