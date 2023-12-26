class Solution:
    def mySqrt(self, x: int) -> int:
        num=1
        while True:
            if num*num>x: return num-1
            num+=1
        
