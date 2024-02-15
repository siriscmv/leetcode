class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        l = len(nums)
        
        curr = nums[0]
        prefix_sum = [0]
        for i in range(1, l):
            prefix_sum.append(curr)
            curr += nums[i]
        
        for i in range(l-1, -1, -1):
            if nums[i] < prefix_sum[i]: return prefix_sum[i] + nums[i]
        
        return -1
