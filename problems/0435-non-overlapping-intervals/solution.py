class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        ans, curr = 0, float("-inf")
        
        for a, b in intervals:
            if a < curr:
                ans += 1
                curr = min(curr, b)
            else: curr = b
        
        return ans    
