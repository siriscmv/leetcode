class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans, l, prev = 0, len(prices), -1
        mx = [0] * l

        for i in range(l-1, -1, -1):
            mx[i] = prev
            prev = max(prev, prices[i])
        
        for i in range(l): ans = max(ans, mx[i] - prices[i])
        return ans
