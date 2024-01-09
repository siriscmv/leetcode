class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.invert(root)
        return root
    
    def invert(self, root):
        if not root: return
        root.left, root.right = root.right, root.left
        self.invert(root.left)
        self.invert(root.right)
