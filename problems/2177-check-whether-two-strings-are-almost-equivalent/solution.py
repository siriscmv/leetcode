from collections import defaultdict

class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        counts = defaultdict(lambda: [0, 0])
        for c in word1: counts[c][0]+=1
        for c in word2: counts[c][1]+=1
        return all([abs(a-b)<=3 for a,b in counts.values()])
