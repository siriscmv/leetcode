from collections import defaultdict

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        c1, c2 = defaultdict(int), defaultdict(int)
        
        for ch in word1: c1[ch] += 1
        for ch in word2: c2[ch] += 1

        a1, a2 = map(sorted, zip(*list(c1.items())))
        b1, b2 = map(sorted, zip(*list(c2.items())))
        
        return a1 == b1 and a2 == b2
