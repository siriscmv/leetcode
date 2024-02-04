class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        mp, seen, words = {}, set(), s.split(' ')
        if len(pattern) != len(words): return False
        
        for i, ch in enumerate(pattern):
            if ch in mp:
                if mp[ch] != words[i]: return False
            elif words[i] in seen: return False
            else: 
                mp[ch] = words[i]
                seen.add(words[i])
        
        return True
