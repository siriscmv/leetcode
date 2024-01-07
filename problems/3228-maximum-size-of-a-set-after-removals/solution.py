from collections import defaultdict

class Solution:
    def maximumSetSize(self, nums1: List[int], nums2: List[int]) -> int:
        counts = defaultdict(lambda: [0, 0])
        
        for n in nums1: counts[n][0] += 1
        for n in nums2: counts[n][1] += 1
        
        n = len(nums1)
        a, b = n//2, n//2
        
        st = sorted(counts.values(), key=lambda x: x[0]+x[1], reverse=True)
        i, l = 0, len(st)
        
        while (a>0 or b>0) and i<l: # Reduce to 1 greedy
            if a>0 and st[i][0] > 1:
                a -= st[i][0] - 1
                st[i][0] = 1
            if b>0 and st[i][1] > 1:
                b -= st[i][1] - 1
                st[i][1] = 1
            i += 1
        
        i, left, right = 0, sum([1 for a in st if a[0] >= 1]), sum([1 for a in st if a[1] >= 1])
        while (a>0 or b>0) and i<l: # reduce to 1 if other exists
            if a>0 and st[i][0] == 1 and st[i][1] >= 1 and left>=right:
                left -= 1
                a -= 1
                st[i][0] = 0
            if b>0 and st[i][1] == 1 and st[i][0] >= 1 and right>=left:
                right -= 1
                b -= 1
                st[i][1] = 0
            i += 1
        
        i=0
        while (a>0 or b>0) and i<l:
            if a>0 and st[i][0] == 1 and st[i][1] == 0 and left>=right:
                left -= 1
                a -= 1
                st[i][0] = 0
            if b>0 and st[i][1] == 1 and st[i][0] == 0 and right>=left:
                right -= 1
                b -= 1
                st[i][1] = 0
            i += 1
            
        return sum([min(s[0] + s[1], 1) for s in st]) - max(a, 0) - max(b, 0)
