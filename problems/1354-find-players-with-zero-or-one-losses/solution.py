from collections import defaultdict

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        seen, lost = set(), defaultdict(int)
        
        for w, l in matches:
            seen.add(w)
            seen.add(l)
            lost[l] += 1
        
        ans = [[s for s in seen if lost[s] == 0], [l for l in lost if lost[l] == 1]]
        ans[0].sort()
        ans[1].sort()
        
        return ans 
