class Solution:
    def largestInteger(self, num: int) -> int:
      digits, new = [], []
      while num > 0:
        digits.append(num % 10)
        num //= 10
      digits = digits[::-1]
      sdigits = sorted(digits, reverse=True)

      for digit in digits:
        ix = next(i for i,v in enumerate(sdigits) if v != -1 and v%2 == digit%2)
        new.append(sdigits[ix])
        sdigits[ix] = -1
      
      ans = 0
      for n in new: ans = ans*10 + n
      return ans
