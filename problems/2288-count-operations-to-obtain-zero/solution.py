class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        a, b = max(num1, num2), min(num1,num2)
        ans = 0

        while a and b:
            ans += a // b
            a, b = b, a % b
        return ans
        
