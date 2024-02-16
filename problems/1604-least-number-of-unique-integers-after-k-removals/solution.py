class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        counts = defaultdict(int)
        for num in arr: counts[num] += 1

        counts = sorted(counts.values())
        i, l = 0, len(counts)
        
        while k:
            if k < counts[i]: break

            k -= counts[i]
            i += 1
        
        return l - i
