class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
      i, n, seen = 0, len(A), set()
      ans = [0] * n
      
      while i<n:
        if i > 0: ans[i] += ans[i-1]
        a, b = A[i], B[i]
        if a in seen: 
          seen.remove(a)
          ans[i] += 1
        else: seen.add(a)
        if b in seen:
          seen.remove(b)
          ans[i] += 1
        else: seen.add(b)
        i += 1

      return ans
