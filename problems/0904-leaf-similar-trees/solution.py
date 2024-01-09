class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
      return self.dfs(root1) == self.dfs(root2)

    def dfs(self, root):
      leaves = []
      if not root: return leaves
      if not root.left and not root.right: leaves.append(root.val)
      leaves += self.dfs(root.left)
      leaves += self.dfs(root.right)
      return leaves
