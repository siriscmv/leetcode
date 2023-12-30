class Solution:
    def isValid(self, s: str) -> bool:
        m = {"{": "}", "(": ")", "[": "]"}
        stack = []
        for char in s:
            if char in m: stack.append(char)
            elif len(stack) > 0:
                c = stack.pop()
                if c not in m or m[c] != char: return False 
            else: return False
        return len(stack) == 0
        
