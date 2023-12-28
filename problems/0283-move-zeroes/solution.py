class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        curr = len(nums)-1
        while curr >= 0:
            if nums[curr] == 0:
                del nums[curr]
                nums.append(0)
            curr -= 1 
