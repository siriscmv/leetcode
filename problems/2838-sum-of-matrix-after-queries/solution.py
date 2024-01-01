class Solution:
    def matrixSumQueries(self, n: int, queries: List[List[int]]) -> int:
      ans, rows, cols = 0, set(), set()

      for q in queries[::-1]:
        t, i, v = q
        if t == 0 and i not in rows:
          rows.add(i)
          ans += v*(n-len(cols)) 
        elif t == 1 and i not in cols:
          cols.add(i)
          ans += v*(n-len(rows)) 
      
      return ans
