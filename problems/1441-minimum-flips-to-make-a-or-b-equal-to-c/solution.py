class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        l = list(map(lambda n: format(n, 'b'), [a, b, c]))
        m = max([len(n) for n in l])
        a, b, c = [map(int, n.zfill(m)) for n in l]
        ans = 0

        for i, j, l in zip(a, b, c):
            if l and not i and not j: ans += 1
            if not l and i: ans += 1
            if not l and j: ans += 1
        
        return ans
