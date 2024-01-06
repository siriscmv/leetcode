from bisect import bisect_left

class Solution:
    dp = {}
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
      global dp
      dp, jobs = {}, sorted(zip(startTime, profit, endTime))

      return self.getProfit(jobs, 0)

    def getProfit(self, jobs, i):
      global dp
      if i == len(jobs): return 0
      if i in dp: return dp[i]

      j = bisect_left(jobs, jobs[i][2], lo=i+1, key=lambda job: job[0])
      dp[i] = max(self.getProfit(jobs, i+1), jobs[i][1] + self.getProfit(jobs, j))
      return dp[i]
