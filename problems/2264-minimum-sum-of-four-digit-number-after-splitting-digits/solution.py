class Solution:
    def minimumSum(self, num: int) -> int:
        l = sorted(map(int, list(str(num))))
        return sum(l[:2])*10 + sum(l[2:])
