class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        a, b = -prices[0], 0
        for i in range(1, len(prices)):
            aa = a
            a = max(a, b - prices[i])
            b = max(b, aa + prices[i] - fee)
        
        return max(a, b)
