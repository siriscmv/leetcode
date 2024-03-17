class Solution:
    def insert(self, intervals, newInterval):
        ans = []
        
        intervals.append(newInterval)
        intervals.sort()
        
        for interval in intervals:
            if len(ans) == 0 or ans[-1][1] < interval[0]: ans.append(interval)
            elif ans[-1][1] >= interval[0]: ans[-1][1] = max(ans[-1][1], interval[1])
        
        return ans
