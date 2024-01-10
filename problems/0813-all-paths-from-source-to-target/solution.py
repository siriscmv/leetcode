class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n, ans, stack = len(graph), [], [[0]]
        while stack:
            path = stack.pop()
            for node in graph[path[-1]]:
                if node == n-1: ans.append(path + [node])
                else: stack.append(path + [node])
        
        return ans
