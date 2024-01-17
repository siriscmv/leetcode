from collections import defaultdict

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counts, seen = defaultdict(int), set()
        
        for num in arr: counts[num] += 1
        for val in counts.values():
            if val in seen: return False
            seen.add(val)

        return True
