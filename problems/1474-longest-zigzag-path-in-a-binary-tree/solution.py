class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.ans = 0

        self.dfs(root, 1, 0)
        self.dfs(root, -1, 0)

        return self.ans

    def dfs(self, node, dir, length):
        if not node: return
        self.ans = max(self.ans, length)

        if dir == 1:
            self.dfs(node.left, -1, length + 1)
            self.dfs(node.right, 1, 1)
        else:
            self.dfs(node.right, 1, length + 1)
            self.dfs(node.left, -1, 1)
