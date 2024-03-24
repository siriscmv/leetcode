class Solution:
    def minOperations(self, k: int) -> int:
        sq = ceil( k ** 0.5)
        
        ans = sq-1
        
        ans += ceil(k/sq-1)
        
        return ans
