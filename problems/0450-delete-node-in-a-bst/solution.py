class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        searched = self.search(root, key)
        if not searched: return root

        parent, node_to_delete = searched
        children_count = self.get_children_count(node_to_delete)

        if children_count == 0:
            if not parent: return None
            if key < parent.val: parent.left = None
            else: parent.right = None

        elif children_count == 1:
            if not parent: return root.left or root.right
            new_node = node_to_delete.left or node_to_delete.right
            if key < parent.val: parent.left = new_node
            else: parent.right = new_node

        elif children_count == 2:
            right_inorder_key = self.get_right_inorder(node_to_delete).val
            self.deleteNode(root, right_inorder_key)
            node_to_delete.val = right_inorder_key

        return root
    
    def search(self, node, key):
        if not node: return False
        if node.val == key: return (None, node)
        
        if key < node.val:
            if node.left and node.left.val == key: return (node, node.left)
            return self.search(node.left, key)
        else:
            if node.right and node.right.val == key: return (node, node.right)
            return self.search(node.right, key)

    def get_children_count(self, node):
        s = 0
        if node.left: s += 1
        if node.right: s += 1
        return s
    
    def get_right_inorder(self, node):
        ans = node.right
        if not ans: return None

        while ans.left: ans = ans.left
        return ans
