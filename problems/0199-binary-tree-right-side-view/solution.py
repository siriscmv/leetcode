from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        stack = [[root]]

        while True:
            prev = stack[-1]
            t = []
            for node in prev:
                if node.left: t.append(node.left)
                if node.right: t.append(node.right)
            if t: stack.append(t)
            else: break
        
        return [row[-1].val for row in stack]
