class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        c = ans = i = j = 0
        nxt, l = None, len(nums)
        
        while i<l and j<l:
            if nums[j] == 0:
                if c == 1: 
                    ans = max(ans, j-i-c)
                    if nxt: i = nxt
                    else: i = j
                    nxt = None
                else: c += 1
            elif c == 1 and nxt == None: nxt = j
            j += 1
        
        ans = max(ans, j-i-c)
        if ans == l: ans -= 1
        return ans
