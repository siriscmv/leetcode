class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        ans, last, l = 0, -2, len(flowerbed)

        for i, plot in enumerate(flowerbed):
            if plot == 1:
                last = i
            elif i-last > 1 and (i == l-1 or not flowerbed[i+1]): 
                last = i
                ans += 1
        
        return ans >= n
