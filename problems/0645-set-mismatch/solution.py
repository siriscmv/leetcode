class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
      st, n = set(nums), len(nums)
      ans = None
      
      for i in range(1, n+1):
        if i not in st:
          ans = i
          break
      
      return [ans + sum(nums) - n*(n+1)//2 , ans]
