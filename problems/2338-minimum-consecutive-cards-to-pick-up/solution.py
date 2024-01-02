from collections import defaultdict

class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        pos = defaultdict(list)
        for i, card in enumerate(cards): pos[card].append(i)

        ans = float('inf')
        for p in pos:
          l = len(pos[p])
          if l < 2: continue
          for i in range(0, l-1): ans = min(ans, pos[p][i+1] - pos[p][i] + 1)
        return ans if ans != float('inf') else -1
