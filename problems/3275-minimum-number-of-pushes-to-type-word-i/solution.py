from math import ceil

class Solution:
    def minimumPushes(self, word: str) -> int:
        s, c = len(word)//8, 1
        ans = 0
        
        for i in range(s): 
            ans += 8*c
            c += 1
        
        ans += (len(word) % 8)*c
        return ans
        
