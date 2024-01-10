class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
      return self.solve(root)
    
    def solve(self, root, is_left = False):
        if not root: return 0
        s = 0
        if not(root.left or root.right) and is_left: s += root.val
        s += self.solve(root.left, True)
        s += self.solve(root.right)
        return s
