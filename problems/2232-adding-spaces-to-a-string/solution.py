class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
      if len(spaces) == 0: return s
      ans = [s[:spaces[0]]]
      for i in range(0, len(spaces)-1): ans.append(s[spaces[i]:spaces[i+1]])
      ans.append(s[spaces[len(spaces)-1]:])
      return " ".join(ans)
