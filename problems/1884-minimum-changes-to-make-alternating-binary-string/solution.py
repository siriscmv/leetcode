import math

class Solution:
    def getDiff(self, s: str, c: str):
        count=0
        for i, char in enumerate(s):
            if c[i] != char: count+=1
        return count

    def minOperations(self, s: str) -> int:
        l = math.ceil(len(s) / 2)
        c1, c2 = "01"*l, "10"*l

        return min(self.getDiff(s, c1), self.getDiff(s, c2))
