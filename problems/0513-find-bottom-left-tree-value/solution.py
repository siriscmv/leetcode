class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        queue = deque([root])
        ans = None

        while queue:
            node = queue.popleft()
            ans = node.val

            if node.right: queue.append(node.right)
            if node.left: queue.append(node.left)

        return ans
