class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        n = len(grid)
        for i, row in enumerate(grid):
            ans = True
            for j, cell in enumerate(row):
                if cell == 0 and i != j: 
                    ans = False
                    break
            if ans: return i
