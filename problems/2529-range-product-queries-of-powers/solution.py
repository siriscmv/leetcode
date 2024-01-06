from math import log

class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
      powers, curr = [], 0
      mod = 10 ** 9 + 7
      while curr < n:
        c = 2 ** int(log(n-curr, 2))
        powers.append(c)
        curr += c
      
      pp, curr = {}, 1
      for i, p in enumerate(powers[::-1]):
        curr *= p
        pp[i] = curr
      pp[-1] = 1
      
      return [(pp[r] // pp[l-1]) % mod for l, r in queries]
