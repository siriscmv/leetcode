class Solution(object):
    def sumCounts(self, nums):
        ans, l = 0, len(nums)
        
        for i in range(1, l+1):
            for j in range(0, l-i+1):
                ans += len(set(nums[j:i+j])) ** 2
        
        return ans  
