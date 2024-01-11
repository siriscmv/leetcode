class Solution:
    def compress(self, chars: List[str]) -> int:
        i, l = 0, len(chars)

        while i<l:
            if i == l-1 or chars[i+1] != chars[i]: pass
            else:
                c = 0
                for j in range(i, l):
                    if j < l and chars[j] == chars[i]: c += 1
                    else: break
                
                for d in str(c):
                    i += 1
                    chars[i] = d
                
                removed = c - 1 - len(str(c))
                l -= removed
                for _ in range(i+1, i+1+removed): del chars[i+1]
            i += 1

        return l    
