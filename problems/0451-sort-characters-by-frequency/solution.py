class Solution:
    def frequencySort(self, s: str) -> str:
        counts = defaultdict(int)
        for ch in s: counts[ch] += 1

        return "".join([ch * c for ch, c in sorted(counts.items(), key=lambda x: -x[1])])
