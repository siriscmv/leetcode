class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        l, ans = len(nums), 0
        for i, num in enumerate(nums):
            if l-i <= ans: return ans
            if num>threshold or num%2 != 0: continue
            j=1
            while i+j<l and nums[i+j]<=threshold and j%2 == nums[i+j]%2: j += 1
            ans = max(ans, j)
        return ans
