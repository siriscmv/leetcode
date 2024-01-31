from collections import defaultdict

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        ans = float('inf')
        graph = defaultdict(set)

        for a, b, d in roads:
            graph[a].add((b, d))
            graph[b].add((a, d))

        def dfs(node, seen):
            nonlocal ans
            seen.add(node)
            for n, d in graph[node]:
                ans = min(ans, d)
                if n not in seen: dfs(n, seen)
        
        dfs(1, set())
        return ans
