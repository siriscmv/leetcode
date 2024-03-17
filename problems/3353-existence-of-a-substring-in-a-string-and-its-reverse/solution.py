class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        rev = s[::-1]
        ln = len(s)
        
        for i in range(ln-1):
            try:
                if s[i:i+2] in rev: return True
            except: pass
        
        return False
