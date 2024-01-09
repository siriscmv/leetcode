class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
      l, lr, rl = len(nums), [], []
      t1, t2 = 0, 0
      for i in range(l):
        lr.append(t1)
        t1 += nums[i]
        rl.append(t2)
        t2 += nums[l-1-i]
      
      rl = rl[::-1]
      return [nums[i] * i - nums[i] * (l-1-i) + rl[i] - lr[i] for i in range(l)] 
