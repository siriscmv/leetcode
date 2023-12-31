class Solution:
    def countPoints(self, rings: str) -> int:
        rods = [{'R', 'G', 'B'} for _ in range(0,10)]
        i, l = 0, len(rings)
        
        while i<l:
            c, r = rings[i], int(rings[i+1])
            rods[r] -= {c}
            i += 2
        
        return len([s for s in rods if len(s) == 0])
