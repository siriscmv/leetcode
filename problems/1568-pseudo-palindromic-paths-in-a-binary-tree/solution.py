class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        return self.solve(root, set())
    
    def solve(self, node, path):
        if node.val in path: path.remove(node.val)
        else: path.add(node.val)

        if not (node.left or node.right): return 1 if len(path) <= 1 else 0
        
        ans = 0
        if node.left: ans += self.solve(node.left, set(path))
        if node.right: ans += self.solve(node.right, set(path))
        return ans
