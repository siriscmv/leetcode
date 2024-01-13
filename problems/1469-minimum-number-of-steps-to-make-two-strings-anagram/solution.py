from collections import defaultdict

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        counts = defaultdict(int)

        for ch in s: counts[ch] += 1
        for ch in t: counts[ch] -= 1

        return sum([abs(v) for v in counts.values()]) // 2
