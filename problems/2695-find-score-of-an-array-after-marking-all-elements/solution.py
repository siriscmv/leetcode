class Solution:
    def findScore(self, nums: List[int]) -> int:
      score, marked, nums = 0, set(), sorted(enumerate(nums), key=lambda x: (x[1], x[0]))

      for i, v in nums:
        if i in marked: continue
        
        score += v
        marked.add(i-1)
        marked.add(i)
        marked.add(i+1)
      
      return score
