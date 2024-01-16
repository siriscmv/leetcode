from collections import defaultdict

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        known, graph, vals = set(), defaultdict(set), {}

        for (x, y), v in zip(equations, values):
            known.add(x)
            known.add(y)
            graph[x].add(y)
            graph[y].add(x)
            vals[(x, y)] = v
            vals[(y, x)] = 1 / v
        
        return [self.dfs(graph, vals, known, x, y, set()) for x, y in queries]
    
    def dfs(self, graph, vals, known, x, y, seen):
        if x not in known: return -1
        if y not in known: return -1
        if x == y: return 1
        seen.add(x)

        for n in graph[x]:
            if n in seen: continue
            res = self.dfs(graph, vals, known, n, y, seen)
            if res == -1: continue
            return vals[(x, n)] * res
        
        return -1
