from math import inf

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        i, j = 0, len(nums) - 1

        while i <= j:
            mid = (i + j) // 2
            a, b, c = nums[mid - 1] if mid-1 >= 0 else -inf, nums[mid], nums[mid + 1] if mid+1 < len(nums) else -inf

            if a < b > c: return mid
            if a >= b: j = mid - 1
            else: i = mid + 1
