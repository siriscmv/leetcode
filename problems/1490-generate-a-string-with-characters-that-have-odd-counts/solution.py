class Solution:
    def generateTheString(self, n: int) -> str:
        l = n-1 if n%2 == 0 else n
        return "".join(['a']*l + ['b']*(n-l))
        
