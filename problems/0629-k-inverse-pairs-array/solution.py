class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        return self.f(n, k)
    
    @cache
    def f(self, n, k):
        if not k: return 1
        if k < 0 or n <= 0: return 0

        return (self.f(n-1, k) + self.f(n, k-1) - self.f(n-1, k-n)) % (10 ** 9 + 7)
