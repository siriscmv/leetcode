class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root: return 0

        ans = 0
        ans += self.solve(root, targetSum)
        ans += self.pathSum(root.left, targetSum)
        ans += self.pathSum(root.right, targetSum)

        return ans

    def solve(self, node, target):
        ans = 0
        if not node: return 0
        if node.val == target: ans += 1

        ans += self.solve(node.left, target - node.val)
        ans += self.solve(node.right, target - node.val)

        return ans
