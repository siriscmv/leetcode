from math import ceil

class Solution:
    def minimumPushes(self, word: str) -> int:
        freq = {}
        for char in range(ord('a'), ord('z') + 1): freq[chr(char)] = 0
        for ch in word: freq[ch] += 1
            
        st = sorted([(c, freq[c]) for c in freq], key=lambda x: -x[1])
        keypad = {}
        curr = 1
        for char, _ in st: 
            keypad[char] = ceil(curr / 8)
            curr += 1
        
        return sum([keypad[w] for w in word])
