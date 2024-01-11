class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = len(height)
        i, j, ans = 0, l-1, 0

        while i < j:
            vol = (j-i) * min(height[i], height[j])
            ans = max(ans, vol)
            if height[i] > height[j]: j -= 1
            elif height[i] < height[j]: i += 1
            else:
                i += 1
                j -= 1
        return ans
            
        
