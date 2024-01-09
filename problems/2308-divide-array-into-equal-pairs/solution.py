from collections import defaultdict

class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        counts = defaultdict(int)
        for num in nums: counts[num] += 1
        return all([n % 2 == 0 for n in counts.values()])
