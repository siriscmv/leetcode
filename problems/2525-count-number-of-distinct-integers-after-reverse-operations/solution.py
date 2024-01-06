class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
      st = set(nums)
      for n in nums: st.add(int(str(n)[::-1]))
      return len(st)        
