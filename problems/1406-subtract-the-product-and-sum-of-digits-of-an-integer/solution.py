class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        p, s = 1, 0
        if n == 0: return 0
        while n>0:
            d = n%10
            p *= d
            s += d
            n //= 10
        return p-s
        
