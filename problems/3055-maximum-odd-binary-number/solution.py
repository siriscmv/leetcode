class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        a, b = s.count('1'), s.count('0')

        return '1' * (a-1) + '0' * b + '1'
