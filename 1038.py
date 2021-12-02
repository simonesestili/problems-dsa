class Solution:
    def bstToGst(self, root):
        self.total = 0

        def inorder(node):
            if not node: return
            inorder(node.right)
            self.total += node.val
            node.val = self.total
            inorder(node.left)

        inorder(root)
        return root
