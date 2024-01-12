class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return self.solve(root, set())
    
    def solve(self, node, path):
        if not node: return 0
        c = 0
        
        if all([n <= node.val for n in path]): c += 1
        path.add(node.val)

        c += self.solve(node.left, path.copy()) + self.solve(node.right, path.copy())
        return c
