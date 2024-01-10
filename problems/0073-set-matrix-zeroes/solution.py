class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows, cols = set(), set()
        m, n = len(matrix), len(matrix[0]) 

        for i, row in enumerate(matrix):
            for j, cell in enumerate(row):
                if not cell:
                    rows.add(i)
                    cols.add(j)
        
        for r in rows: matrix[r] = [0] * n
        for c in cols:
            for i in range(m): matrix[i][c] = 0
