class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        a, b = s.count('0'), s.count('1')
        return '1' * (b-1) + '0' * a + '1'
