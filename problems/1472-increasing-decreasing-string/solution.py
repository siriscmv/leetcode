from itertools import groupby
from collections import defaultdict

class Solution:
    def sortString(self, s: str) -> str:
        ans, counts, chrs = [], defaultdict(int), []
        for char, itr in groupby(s): counts[char] += len(list(itr))
        for c in counts: chrs.append(c)
        
        lr = sorted(chrs)
        rl = sorted(chrs, reverse=True)
        found, i, l = True, 1, len(counts)
        
        while found:
            found=False
            lst = lr if i%2 == 1 else rl
            for ch in lst:
                cnt = counts[ch]
                if cnt == 0: continue
                found=True
                ans.append(ch)
                counts[ch] -= 1
            i += 1
        
        return "".join(ans)        
