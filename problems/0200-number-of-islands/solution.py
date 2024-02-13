class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited, count = set(), 0

        def flood(x, y): 
            if (x, y) in visited: return
            if x<0 or y<0 or x>=len(grid) or y>=len(grid[0]): return
            if grid[x][y] != '1': return
        
            visited.add((x, y))
            flood(x+1, y)
            flood(x-1, y)
            flood(x, y+1)
            flood(x, y-1)

        for r, line in enumerate(grid):
            for c, cell in enumerate(line):
                if (r, c) in visited: continue

                if cell == '1': 
                    flood(r, c)
                    count += 1
        
        return count
