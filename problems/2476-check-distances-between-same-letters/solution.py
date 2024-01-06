class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        space = {}
        for i, char in enumerate(s):
          c = ord(char) - ord('a')
          if c not in space: space[c] = i
          else: space[c] = i - space[c] - 1
        
        return all([i not in space or space[i] == d for i, d in enumerate(distance)])
