class Solution:
    def countVowels(self, word: str) -> int:
      ans, l = 0, len(word)
      VOWELS = ['a', 'e', 'i', 'o', 'u']
      
      for i, ch in enumerate(word):
        if ch not in VOWELS: continue
        ans += (i+1) * (l-i)
      
      return ans
