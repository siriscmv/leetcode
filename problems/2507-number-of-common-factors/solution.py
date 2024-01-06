class Solution:
    def hcf(self, a, b):
      while b: a, b = b, a % b
      return a
    
    def commonFactors(self, a: int, b: int) -> int:
      hcf = self.hcf(a, b)
      return sum([1 for i in range(1, hcf+1) if hcf%i == 0])
        
