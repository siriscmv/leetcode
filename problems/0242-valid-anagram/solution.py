class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        c = defaultdict(int)

        for ch in s: c[ch] += 1
        for ch in t: c[ch] -= 1

        return all([not c[ch] for ch in c])
