class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        if not nums: return 0
        
        counts = defaultdict(int)
        for n in nums: counts[n] += 1
        
        maxx = max(counts.values())
        return sum([n for n in counts.values() if n == maxx])
