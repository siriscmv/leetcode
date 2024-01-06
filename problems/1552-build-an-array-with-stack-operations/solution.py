class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
      ans, curr = [], 0
      for t in target:
          ans += [1, -1] * (t-curr-1)
          ans += [1]
          curr = t
      
      return ["Push" if a == 1 else "Pop" for a in ans]
