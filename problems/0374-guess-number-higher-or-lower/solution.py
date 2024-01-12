class Solution:
    def guessNumber(self, n: int) -> int:
        l, r = 1, n
        
        while l <= r:
            mid = (l + r) // 2
            g = guess(mid)

            if g == -1: r = mid - 1
            elif g == 1: l = mid + 1
            else: return mid
