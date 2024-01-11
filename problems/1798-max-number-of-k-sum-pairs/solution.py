class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans, i, j = 0, 0, len(nums) - 1

        while i < j:
            s = nums[i] + nums[j]
            if s <= k: i += 1
            if s >= k: j -= 1
            if s == k: ans += 1
        
        return ans
