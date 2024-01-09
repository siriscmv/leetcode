class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.solve(root, 0)
    
    def solve(self, root, level):
        if not root: return level
        return max(self.solve(root.left, level+1), self.solve(root.right, level+1))
