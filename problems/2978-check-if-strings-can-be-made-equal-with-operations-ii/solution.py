class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
      a = sorted(s1[0::2]) + sorted(s1[1::2])
      b = sorted(s2[0::2]) + sorted(s2[1::2])
      return a == b
