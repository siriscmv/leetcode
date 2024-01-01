from itertools import groupby

class Solution:
    def maxPower(self, s: str) -> int:
        return max([len(list(c)) for _, c in groupby(s)])        
