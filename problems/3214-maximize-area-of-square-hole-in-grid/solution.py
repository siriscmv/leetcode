class Solution:
    def getSizes(self, bars):
        sizes, prev, cont = {1}, None, 1
        if len(bars) >= 1: sizes.add(2)

        for bar in bars:
            if prev and bar == prev+1: 
                cont += 1
                sizes.add(cont+1)
            else: cont = 1
            prev = bar
        
        return sizes

    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        h, v = self.getSizes(sorted(hBars)), self.getSizes(sorted(vBars))
        return max(h&v) ** 2
