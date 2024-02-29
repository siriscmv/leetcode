class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        q = deque([(0, root)])
        prev = (None, None)

        while q:
            level, node = q.popleft()

            if node.left: q.append((level+1, node.left))
            if node.right: q.append((level+1, node.right))

            if level % 2 == 0:
                if node.val % 2 == 0: return False
                if level == prev[0] and node.val <= prev[1]: return False
            else:
                if node.val % 2: return False
                if level == prev[0] and node.val >= prev[1]: return False

            prev = (level, node.val)

        return True
