class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans, curr = [1], 1
        for num in nums[0:-1]:
            curr *= num
            ans.append(curr)
        
        i, curr = len(nums) - 2, 1
        for num in reversed(nums[1:]):
            curr *= num
            ans[i] *= curr
            i -= 1
        return ans


