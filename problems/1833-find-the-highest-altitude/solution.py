class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        ans, prev = 0, 0
        
        for g in gain:
            prev += g
            ans = max(ans, prev)
        
        return ans
        
