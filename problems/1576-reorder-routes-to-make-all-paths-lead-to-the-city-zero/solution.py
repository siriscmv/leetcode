from collections import defaultdict

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        ans, seen, graph, ug = 0, set(), defaultdict(set), defaultdict(set)
        for a, b in connections: 
            graph[a].add(b)
            ug[a].add(b)
            ug[b].add(a)

        stack = [0]
        while stack:
            node = stack.pop()
            seen.add(node)

            for n in ug[node]:
                if n not in seen:
                    if node not in graph[n]: 
                        ans += 1
                        graph[n].add(node)
                    stack.append(n)
        
        return ans
