class Solution:
    def has_zero(self, n):
        while n>0:
            if n%10 == 0: return True
            n //= 10
        return False

    def getNoZeroIntegers(self, n: int) -> List[int]:
        i=1
        while i<=n//2:
            if not self.has_zero(i) and not self.has_zero(n-i):
                return [i, n-i] 
            i += 1
        return [-1, -1]
        
