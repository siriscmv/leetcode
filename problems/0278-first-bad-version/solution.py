# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
      s, e = 1, n
      while s<=e:
        mid = (s+e) // 2
        if isBadVersion(mid): 
          if mid-s == 0 or e-mid == 0: return mid
          e = mid-1
        else: s = mid+1
      return s
