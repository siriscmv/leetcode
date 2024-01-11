class Solution:
    def reverseVowels(self, s: str) -> str:
        VOWELS = set(['a', 'e', 'i', 'o', 'u'])
        vowels = [i for i, ch in enumerate(s) if ch.lower() in VOWELS]

        l, ans = len(vowels), list(s)
        for i in range(0, l // 2):
            a, b = vowels[i], vowels[l-i-1]
            ans[a], ans[b] = s[b], s[a]

        return "".join(ans) 

        
