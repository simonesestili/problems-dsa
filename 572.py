class Solution:
    def isSubtree(self, root, subRoot):
        if not root:
            return False
        return (root.val == subRoot.val and self.equals(root, subRoot) or
                self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))
    
    def equals(self, root1, root2):
        if not root1 or not root2:
            return root1 == root2
        return root1.val == root2.val and self.equals(root1.left, root2.left) and self.equals(root1.right, root2.right)
