class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [[] for _ in range(9)]
        cols = [[] for _ in range(9)]
        cells = [[] for _ in range(9)]

        for i in range(0, 9):
            for j in range(0, 9):
                tile = board[i][j]
                if tile == '.': continue
                
                tile = int(tile) 
                key = i//3 * 3 + j//3
                if tile in rows[i] or tile in cols[j] or tile in cells[key]: return False
                
                rows[i].append(tile)
                cols[j].append(tile)
                cells[key].append(tile)

        return True
