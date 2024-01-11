from math import inf

class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        ans, stack = 0, [root]
        while stack:
            node = stack.pop()
            ans = max(ans, self.solve(node, node.val))
            if node.left: stack.append(node.left)
            if node.right: stack.append(node.right)
        
        return ans

    def solve(self, start, a):
        if start == None: return 0
        ans = abs(a - start.val)
        l, r = self.solve(start.left, a), self.solve(start.right, a)
        
        return max(ans, l, r) 
