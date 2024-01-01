class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        seen, ans = set(), 0

        for r, row in enumerate(grid):
            curr = []
            for c, cell in enumerate(row): 
                if cell == 1: curr.append((r, c))
            if len(curr) <= 1: continue
            for cur in curr:
                if cur not in seen: ans += 1
                seen.add(cur)
        
        for c, col in enumerate(zip(*grid)):
            curr = []
            for r, cell in enumerate(col): 
                if cell == 1: curr.append((r, c))
            if len(curr) <= 1: continue
            for cur in curr:
                if cur not in seen: ans += 1
                seen.add(cur)
        
        return ans
