from collections import defaultdict

class Solution:
    dp = {}

    def dfs(self, start, graph, quiet, path):
      global dp
      if start in path: return None
      if start in dp: return dp[start]

      path.add(start)
      i = start
      
      for n in graph[start]:
        ix = self.dfs(n, graph, quiet, path)
        if ix is not None and quiet[ix] < quiet[i]: i = ix
      
      dp[start] = i
      return i

    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
      global dp
      dp, graph = {}, defaultdict(list)
      for a, b in richer: graph[b].append(a)
      return [self.dfs(i, graph, quiet, set()) for i in range(len(quiet))]
