class Solution:
    def flood(self, r, c, grid):
      if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]): return 0
      val = grid[r][c]
      if val <= 0: return 0
      grid[r][c] = 0
      
      return val + self.flood(r-1, c, grid) + self.flood(r+1, c, grid) + self.flood(r, c-1, grid) + self.flood(r, c+1, grid)
    
    def findMaxFish(self, grid: List[List[int]]) -> int:
      ans = 0
      for r, row in enumerate(grid):
        for c, cell in enumerate(row):
          if cell <= 0: continue
          ans = max(ans, self.flood(r, c, grid))
      
      return ans
