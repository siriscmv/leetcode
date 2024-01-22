class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        return self.solve(1, k, n)
    
    def solve(self, i, k, n):
        if n <= 0: return []
        if k == 1: 
            if n >= i and n < 10: return [[n]]
            else: return []
        ans = []

        for i in range(i, 10):
            for a in self.solve(i+1, k-1, n-i):
                ans.append([i] + a)
        
        return ans
