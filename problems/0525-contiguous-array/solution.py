class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        mp = {}
        ps = ans = 0

        for i, num in enumerate(nums):
            ps += 1 if num == 1 else -1

            if ps == 0: ans = i + 1
            elif ps in mp: ans = max(ans, i - mp[ps])
            else: mp[ps] = i
        
        return ans
