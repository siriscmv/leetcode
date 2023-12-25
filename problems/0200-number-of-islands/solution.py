class Solution:
    visited = set()

    def numIslands(self, grid: List[List[str]]) -> int:
        global visited
        visited, count = set(), 0

        for r, line in enumerate(grid):
            for c, cell in enumerate(line):
                if (r, c) in visited: continue

                if cell == '1': 
                    self.flood(grid, r, c)
                    count += 1
        
        return count

    def flood(self, grid, x, y): 
        if (x, y) in visited: return
        if x<0 or y<0 or x>=len(grid) or y>=len(grid[0]): return
        if grid[x][y] != '1': return
        
        visited.add((x, y))
        self.flood(grid, x+1, y)
        self.flood(grid, x-1, y)
        self.flood(grid, x, y+1)
        self.flood(grid, x, y-1)
