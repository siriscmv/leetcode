class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        if len(nums) == 1: return 1+nums[0]
        st = set(nums)
        i, l, prev, s = 1, len(nums), nums[0], nums[0]
        
        while i<l:
            if nums[i] != prev + 1: break
            s += nums[i]
            prev = nums[i]
            i += 1
        
        for j in range(s, 2501):
            if j not in st: return j

