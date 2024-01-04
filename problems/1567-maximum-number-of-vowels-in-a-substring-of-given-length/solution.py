class Solution:
    def maxVowels(self, s: str, k: int) -> int:
      VOWELS = set(['a', 'e', 'i', 'o', 'u'])
      l = len(s)
      lr, rl, total = [0]*l, [0]*l, 1 if (l>=1 and s[0] in VOWELS) else 0

      for i in range(1, l):
        if s[i] in VOWELS: total += 1
        a, b = s[i-1], s[l-i]
        lr[i] = lr[i-1]
        rl[l-i-1] = rl[l-i]
        if a in VOWELS: lr[i] += 1
        if b in VOWELS: rl[l-i-1] += 1
      
      return max([total - lr[i] - rl[i+k-1] for i in range(l-k+1)])
