class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curr, l = sum(nums[:k]), len(nums)
        ans = curr

        for i in range(1, l-k+1):
            curr += nums[i-1+k] - nums[i-1]
            ans = max(ans, curr)
        
        return ans / k
