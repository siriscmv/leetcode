class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        n = len(points)
        points.sort(key = lambda x:x[1])
        prev = points[0][1]
        count = 1

        for i in range(1, n):
            start, end = points[i]

            if start > prev:
                count += 1
                prev = end
        
        return count
