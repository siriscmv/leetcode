from itertools import groupby

class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
      ans = 0
      lens = [sum(1 for _ in itr) for ch, itr in groupby(nums) if ch == 0]
      return sum(map(lambda n: n*(n+1)//2, lens))
