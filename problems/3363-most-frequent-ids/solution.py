class Solution:
    def mostFrequentIDs(self, nums: List[int], freq: List[int]) -> List[int]:
        vals = []
        ans = []
        
        cache = defaultdict(int)
        
        for n, f in zip(nums, freq):
            e = bisect.bisect_left(vals, (cache[n], n))
            if e == len(vals): 
                vals.append((f, n))
                ans.append(f)
            else:
                if vals[e][1] == n: del vals[e]
                insort(vals, (cache[n]+f, n))
                ans.append(vals[-1][0])
            # print(vals)
            cache[n] += f
        
        return ans
        
