from collections import defaultdict

class Solution:
    pos = None
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        stack, graph = [root], defaultdict(list)
        while stack:
            node = stack.pop()
            if node.left: 
                graph[node.val].append(node.left.val)
                graph[node.left.val].append(node.val)
                stack.append(node.left)
            if node.right: 
                graph[node.val].append(node.right.val)
                graph[node.right.val].append(node.val)
                stack.append(node.right)
        
        seen, time, stack = set([start]), 0, [[start]]
        while stack:
            nxt, nodes = [], stack.pop()
            for node in nodes: nxt.extend([n for n in graph[node] if n not in seen])
            if nxt:
                for n in nxt: seen.add(n)
                stack.append(nxt)
                time += 1

        return time
