from math import ceil

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        a, b, ans = 1, max(piles), None

        while a <= b:
            mid = (a + b) // 2
            t = sum([ceil(p/mid) for p in piles])
            if t > h: a = mid + 1
            else: 
                ans = mid
                b = mid - 1
        return ans
