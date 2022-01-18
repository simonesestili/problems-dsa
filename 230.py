class Solution:
    def kthSmallest(self, root, k):
        self.k = k - 1

        def inorder(node):
            if not node: return
            left = inorder(node.left)
            mid = None if self.k else node.val
            self.k -= 1
            right = inorder(node.right)
            return left if left is not None else mid if mid is not None else right

        return inorder(root)
