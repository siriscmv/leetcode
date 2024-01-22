class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        seen, ans = set(), 0

        for n in nums:
            if n in seen: ans = n
            else: seen.add(n)

        for i in range(1, len(nums)+1):
            if i not in seen: return [ans, i]
