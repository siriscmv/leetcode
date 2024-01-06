class Solution:
    def closetTarget(self, words: List[str], target: str, startIndex: int) -> int:
      i, l = 0, len(words)

      for i in range(0, l):
        if words[(startIndex + i) % l] == target or words[(startIndex-i+l)%l] == target: return i
      return -1
