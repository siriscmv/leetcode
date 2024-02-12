class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def solve(node, curr):
            if not node: return False
            curr += node.val
            if not node.left and not node.right: return curr == targetSum
            return solve(node.left, curr) or solve(node.right, curr)
        
        if not root: return False
        return solve(root, 0)
