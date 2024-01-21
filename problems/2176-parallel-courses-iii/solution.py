from collections import defaultdict

class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        ans, start, graph = 0, set(range(1, n+1)), defaultdict(set)
        max_times = {}
        for i, t in enumerate(time): max_times[i+1] = t

        for a, b in relations: 
            if b in start: start.remove(b)
            graph[a].add(b)
        
        def dfs(node, t):
            nonlocal ans
            tt = t + time[node-1]

            if tt < max_times[node]: return
            else: max_times[node] = tt

            ans = max(ans, tt)
            for n in graph[node]: dfs(n, tt)
        
        for node in start: dfs(node, 0)
        return ans
