from collections import deque

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        start = (entrance[0], entrance[1])
        seen, q = set([start]), deque([(start, 0)])
        m, n = len(maze), len(maze[0])
        MOVES = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while q:
            cell, cost = q.popleft()

            for a, b in MOVES:
                nn = (cell[0] + a, cell[1] + b)

                if nn[0] < 0 or nn[0] >= m: continue
                if nn[1] < 0 or nn[1] >= n: continue
                if maze[nn[0]][nn[1]] == "+": continue
                if nn in seen: continue

                seen.add(nn)
                if nn[0] == 0 or nn[1] == 0 or nn[0] == m-1 or nn[1] == n-1: return cost + 1
                q.append((nn, cost + 1))
        
        return -1
