class Solution:
    def minMovesToCaptureTheQueen(self, a: int, b: int, c: int, d: int, e: int, f: int) -> int:
        rook, bishop, queen = (a, b), (c, d), (e, f)
        
        if abs(bishop[0]-queen[0]) == abs(bishop[1]-queen[1]): 
            l, r, t, bb = min(queen[1], bishop[1]), max(queen[1], bishop[1]), min(queen[0], bishop[0]), max(queen[0], bishop[0])
            if abs(bishop[0]-rook[0]) == abs(bishop[1]-rook[1]) and rook[1] > l and rook[1] < r and rook[0] > t and rook[0] < bb: return 2
            else: return 1
        
        if rook[0]-queen[0] == 0 or rook[1]-queen[1] == 0:
            if rook[0]-queen[0] == 0 and rook[0] == bishop[0] and bishop[1] > min(rook[1], queen[1]) and bishop[1] < max(rook[1], queen[1]): return 2
            if rook[1]-queen[1] == 0 and rook[1] == bishop[1] and bishop[0] > min(rook[0], queen[0]) and bishop[0] < max(rook[0], queen[0]): return 2
            return 1

        return 2
