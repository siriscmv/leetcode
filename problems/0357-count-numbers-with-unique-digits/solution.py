class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0: return 1
        ans = 1
        for i in range(9, 9-n+1, -1): ans *= i
        return ans*9 + self.countNumbersWithUniqueDigits(n-1)
        
