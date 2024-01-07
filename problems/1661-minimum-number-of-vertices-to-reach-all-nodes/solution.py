from collections import defaultdict

class Solution:
    dp = {} 
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
      global dp
      dp, graph, ans, to_visit = {}, defaultdict(set), set(), set(range(n))
      for a, b in edges: graph[a].add(b)
      for i in range(n): graph[i] |= self.dfs(graph, i)
      graph = [(i, nodes) for i, nodes in graph.items()]
      graph.sort(key=lambda x: len(x[1]), reverse=True)
      for i, nodes in graph:
        if nodes & to_visit:
          to_visit -= nodes
          ans.add(i)
          if not to_visit: return list(ans)
      ans |= to_visit
      return list(ans)
    
    def dfs(self, graph, start):
      global dp
      if start in dp: return dp[start]
      path = set([start])
      for node in graph[start]: path |= self.dfs(graph, node)
      dp[start] = path
      return path
