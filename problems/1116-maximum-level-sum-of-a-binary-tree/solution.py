class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        stack = [[root]]

        while True:
            prev = stack[-1]
            t = []
            for node in prev:
                if node.left: t.append(node.left)
                if node.right: t.append(node.right)
            if t: stack.append(t)
            else: break
        
        m = max([sum(map(lambda x: x.val, row)) for row in stack])
        return next(i for i, row in enumerate(stack) if sum(map(lambda x: x.val, row)) == m) + 1
