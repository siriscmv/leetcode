class Solution:
    def differenceOfDistinctValues(self, grid: List[List[int]]) -> List[List[int]]:
      m, n = len(grid), len(grid[0])
      ans = [[0 for _ in range(n)] for _ in range(m)]

      for r, row in enumerate(grid):
        for c, _ in enumerate(row):
          tl, br = set(), set()
          
          i = 1
          while r-i >= 0 and c-i >= 0: 
            tl.add(grid[r-i][c-i])
            i += 1
          
          i = 1
          while r+i < m and c+i < n:
            br.add(grid[r+i][c+i])
            i += 1

          ans[r][c] = abs(len(tl) - len(br))

      return ans
