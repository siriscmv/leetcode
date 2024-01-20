from collections import defaultdict

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freq = defaultdict(int)
        for n in nums: freq[n] += 1

        return sorted(nums, key=lambda n: (freq[n], -n))
