class Solution:
    def get_coords(self, i, j, land):
        a, b = i, j
        m, n = len(land), len(land[0])

        while i+1<m and land[i+1][j]: i += 1
        while j+1<n and land[i][j+1]: j += 1

        for p in range(a, i+1):
            for q in range(b, j+1): land[p][q] = 0

        return [a, b, i, j]

    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        ans = []
        for i, row in enumerate(land):
            for j, cell in enumerate(row):
                if not cell: continue
                ans.append(self.get_coords(i, j, land))
        
        return ans
