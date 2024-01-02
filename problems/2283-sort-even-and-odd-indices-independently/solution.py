class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        l = len(nums)
        for i in range(l-1, 0, -1):
          for j in range(i%2, i, 2):
            if i%2 == 0 and nums[j] > nums[j+2]: nums[j], nums[j+2] = nums[j+2], nums[j]
            elif i%2 != 0 and  nums[j] < nums[j+2]: nums[j], nums[j+2] = nums[j+2], nums[j]
        return nums
