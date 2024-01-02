from collections import defaultdict

class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        counts, seen = defaultdict(int), set()
        
        for user, time in logs:
          if (user, time) in seen: continue
          counts[user] += 1
          seen.add((user, time))
        
        ans = [0] * k
        for user in counts:
          if counts[user] > k: continue
          ans[counts[user]-1] += 1
        
        return ans
