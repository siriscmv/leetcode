class Solution:
    def get_sum(self, r, c, grid):
      rows, cols = len(grid), len(grid[0])
      if r <= 0 or r >= rows-1: return 0
      if c <= 0 or c >= cols-1: return 0

      ans = grid[r][c]
      for cc in range(c-1, c+1+1): ans += grid[r-1][cc] + grid[r+1][cc]
      return ans

    def maxSum(self, grid: List[List[int]]) -> int:
      ans = 0
      for r, row in enumerate(grid):
        for c, cell, in enumerate(row):
          ans = max(ans, self.get_sum(r, c, grid))
      return ans
