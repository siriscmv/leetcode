from collections import defaultdict

class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        freq = defaultdict(int)

        for i in range(0, len(nums)-1):
            if nums[i] == key: freq[nums[i+1]] += 1
        
        m = max([freq[f] for f in freq])
        return next((f for f in freq if freq[f] == m))
