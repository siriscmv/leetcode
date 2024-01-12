class Solution:
    VOWELS = ['a', 'e', 'i', 'o', 'u']
    def halvesAreAlike(self, s: str) -> bool:
        a, b, mid = 0, 0, len(s) // 2

        for i, char in enumerate(s):
            if char.lower() in self.VOWELS:
                if i < mid: a += 1
                else: b += 1
        
        return a == b
