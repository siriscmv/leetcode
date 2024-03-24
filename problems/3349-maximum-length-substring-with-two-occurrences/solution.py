class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        length = len(s)
        
        
        for ln in range(length, 0, -1):
            for i in range(0, length-ln + 1):
                st = s[i:i+ln]
                
                c = defaultdict(int)
                for ch in st: c[ch] += 1
                if all([v <= 2 for v in c.values()]): 
                    return ln
        
        return 0
        
