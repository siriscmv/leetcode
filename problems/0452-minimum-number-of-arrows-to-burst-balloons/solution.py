class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x: (x[0], x[0] - x[1]))
        ans, prev = 1, points[0]

        for i in range(1, len(points)):
            p, q = max(prev[0], points[i][0]), min(prev[1], points[i][1])
            if p <= q: prev = [p, q]
            else: 
                ans += 1
                prev = points[i]
        
        return ans
