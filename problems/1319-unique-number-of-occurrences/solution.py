from collections import defaultdict

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counts = defaultdict(int)
        
        for num in arr: counts[num] += 1
        freq = counts.values()

        return len(freq) == len(set(freq)) 
