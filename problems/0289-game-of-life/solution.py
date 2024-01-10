class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        flip = set()
        m, n = len(board), len(board[0])
        for i, row in enumerate(board):
            for j, cell in enumerate(row):
                live = 0
                for rr in range(max(0, i-1), min(i+1, m-1) + 1):
                    live += board[rr][max(0, j-1):min(j+1, n-1)+1].count(1)
                
                if cell: live -= 1
                if not cell and live == 3: flip.add((i, j))
                elif cell and (live < 2 or live > 3): flip.add((i, j))

        for a,b in flip: board[a][b] = abs(board[a][b] - 1)
