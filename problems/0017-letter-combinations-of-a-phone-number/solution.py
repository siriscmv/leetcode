from collections import deque

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dialpad, ans = {}, deque()
        dialpad['2']="abc"
        dialpad['3']="def"
        dialpad['4']="ghi"
        dialpad['5']="jkl"
        dialpad['6']="mno"
        dialpad['7']="pqrs"
        dialpad['8']="tuv"
        dialpad['9']="wxyz"

        for ch in digits:
            if not ans: 
                ans.extend(list(dialpad[ch]))
                continue

            l = len(ans)
            for _ in range(l):
                prev = ans.popleft()
                ans.extend([prev + c for c in dialpad[ch]])
        
        return ans
