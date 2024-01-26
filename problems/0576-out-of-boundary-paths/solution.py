from functools import cache

class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        @cache
        def dp(x, y, moves):
            if x < 0 or x >= m or y < 0 or y >= n: return 1
            if not moves: return 0

            return sum([dp(x+dx, y+dy, moves-1) for (dx,dy) in [(1,0), (-1,0), (0,1), (0,-1)]])
        
        return dp(startRow, startColumn, maxMove) % (10 ** 9 + 7)
