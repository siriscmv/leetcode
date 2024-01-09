class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        a, b, c = 0, 0, 0
        for move in moves:
            if move == "L": a += 1
            elif move == "R": b += 1
            else: c += 1
        
        return abs(a-b) + c
