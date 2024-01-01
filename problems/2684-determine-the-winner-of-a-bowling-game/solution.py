class Solution:
    def score(self, pins):
      s, prev = 0, [False,False]
      for pin in pins:
        s += 2*pin if any(prev) else pin
        prev[0], prev[1] = prev[1], pin==10 
      return s

    def isWinner(self, player1: List[int], player2: List[int]) -> int:
        a, b = self.score(player1), self.score(player2)
        if a>b: return 1
        elif b>a: return 2
        else: return 0
