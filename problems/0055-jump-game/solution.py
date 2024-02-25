class Solution:
    def canJump(self, nums: List[int]) -> bool:
        l, dest = len(nums), 0

        for i in range(l):
            if i <= dest: dest = max(dest, i + nums[i])
            else: return False

        return dest >= l - 1
