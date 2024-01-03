class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        ans = []
        for num in nums: ans += list(map(lambda x: int(x), str(num)))
        return ans
