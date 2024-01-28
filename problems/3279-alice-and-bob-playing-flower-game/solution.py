class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        a, b = n, m
        if n%2: a += 1
        if m%2: b += 1
        
        return ((a//2) * (m//2)) + ((n//2) * (b//2))
