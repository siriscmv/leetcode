from typing import List

class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        n1, n2 = len(a), len(b)
        
        ans, stack, prev = [], [], None
        
        for i, _ in enumerate(s):
            if s[i:i+n1] == a:
                if prev != None and abs(prev-i) <= k: ans.append(i)
                else: stack.append(i)
            if s[i:i+n2] == b:
                prev = i
                stack = [ss for ss in stack if abs(ss-prev) <= k]
                ans.extend(stack)
                stack = []

        ans.sort()
        return ans

