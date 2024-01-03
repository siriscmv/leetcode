class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
      l, i, ans = len(bank), 0, 0
      while i<l:
        if bank[i].count('1') == 0: 
          i += 1
          continue
        j=i+1
        while j<l and bank[j].count('1') == 0: j += 1
        if j == l: break
        ans += bank[i].count('1') * bank[j].count('1')
        i = j
      return ans
