class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        c = ans = i = j = 0
        nxt, l = None, len(nums)
        
        while i<l and j<l:
            if nums[j] == 0:
                if c == k:
                    ans = max(ans, j-i)
                    i += nums[i:].index(0) + 1
                else: c += 1
            j += 1

        ans = max(ans, j-i)
        return ans
