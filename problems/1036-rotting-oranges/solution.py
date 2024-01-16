class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh, rotten, t = 0, set(), 0
        MOVES = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        m, n = len(grid), len(grid[0])

        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                if cell == 1: fresh += 1
                elif cell == 2: rotten.add((i, j))

        if not rotten and fresh: return -1
        curr = rotten

        while fresh:
            rr = set()
            for a, b in curr:
                for x, y in MOVES:
                    cell = (a+x, b+y)
                    if cell in rotten or cell in rr: continue
                    if cell[0] < 0 or cell[1] < 0: continue
                    if cell[0] >= m or cell[1] >= n: continue
                    if grid[cell[0]][cell[1]] != 1: continue

                    rr.add(cell)
                    fresh -= 1
            
            rotten.update(rr)
            if not rr and fresh: return -1
            curr = rr
            t += 1
        
        return t
