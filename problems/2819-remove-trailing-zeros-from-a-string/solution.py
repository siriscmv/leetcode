class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        if not num.endswith('0'): return num
        return self.removeTrailingZeros(num[:-1])
