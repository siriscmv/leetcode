class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        l1, l2, i, j = len(g), len(s), 0, 0
        while i<l1 and j<l2:
            if s[j]>=g[i]: 
                i += 1
                j += 1
            else: j += 1
        return i
