class Solution:
    def checkString(self, s: str) -> bool:
        prev = 'a'
        for ch in s:
            if prev == ch: pass
            elif prev == 'a': prev = 'b'
            else: return False
        return True
