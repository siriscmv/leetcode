class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        ans = sorted(nums)
        i, l = 0, len(ans)
        while i < l-1:
            ans[i], ans[i+1] = ans[i+1], ans[i]
            i += 2
        return ans
