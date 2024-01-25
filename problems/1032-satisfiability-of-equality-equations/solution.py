from collections import defaultdict

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        graph = defaultdict(set)
        equations.sort(key=lambda x: 0 if x[1] == "=" else 1)

        def dfs(node, target, path):
            if node == target: return True
            path.add(node)
            for n in graph[node]:
                if n not in path and dfs(n, target, path): return True
            return False

        for a, op, _, b in equations:
            if op == "=": 
                graph[a].add(b)
                graph[b].add(a)
            elif dfs(a, b, set()): return False
        
        return True
