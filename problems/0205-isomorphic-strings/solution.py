class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mp, seen, l = {}, set(), len(s)
        if l != len(t): return False

        for i in range(l):
            if s[i] not in mp: 
                if t[i] in seen: return False
                else: 
                    mp[s[i]] = t[i]
                    seen.add(t[i])
            elif mp[s[i]] != t[i]: return False
        
        return True
