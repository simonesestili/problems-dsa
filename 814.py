class Solution:
    def pruneTree(self, root):
        if not root: return None
        root.left, root.right = self.pruneTree(root.left), self.pruneTree(root.right)
        return root if root.left or root.right or root.val else None
