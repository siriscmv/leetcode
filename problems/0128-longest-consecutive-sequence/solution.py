class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums, ans = set(nums), 0

        for num in nums:
            if num-1 in nums: continue
            l, inc = 0, 1
            while num+inc in nums:
                inc += 1
                l += 1
            if l+1 > ans: ans = l+1
        return ans
