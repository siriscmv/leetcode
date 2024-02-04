class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ans, c = None, 0

        for i in range(len(nums)):
            if not c: 
                ans = nums[i]
                c = 1
            elif ans == nums[i]: c += 1
            else: c -= 1
        
        return ans
