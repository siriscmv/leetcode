class Solution:
    def isValid(self, s: str) -> bool:
        brackets = { ")": "(", "}": "{", "]": "[" }
        stack = []

        for ch in s:
            if ch not in brackets: stack.append(ch)
            elif stack and stack[-1] == brackets[ch]: stack.pop()
            else: return False
        
        return not stack
