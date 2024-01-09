from collections import defaultdict

class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        r, s = defaultdict(int), defaultdict(int)
        for rank in ranks: r[rank] += 1
        for suit in suits: s[suit] += 1

        rv, sv = r.values(), s.values()

        if list(sv)[0] == 5: return "Flush"
        if any([r >= 3 for r in rv]): return "Three of a Kind"
        if any([r >= 2 for r in rv]): return "Pair"
        return "High Card"
