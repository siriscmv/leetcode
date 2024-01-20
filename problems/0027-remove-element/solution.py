class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        ans = 0
        for i in range(len(nums)-1, -1, -1):
            if nums[i] == val:
                ans += 1
                nums[i], nums[-ans] = nums[-ans], nums[i]
        
        return len(nums) - ans
