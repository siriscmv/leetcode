class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        def solve(rem):
            ans = 0
            for p in position:
                if p%2 == rem: ans += 1
            return ans
        
        return min(solve(0), solve(1))
