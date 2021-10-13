class Solution:
    def bstFromPreorder(self, preorder):
        root = TreeNode(val=preorder[0])
        self.bst(root, preorder)
        return root

    def bst(self, root, preorder):
        if not root:
            return
        left, right = [], []
        for val in preorder[1:]:
            if val < root.val:
                left.append(val)
            else:
                right.append(val)
        root.left = None if not left else TreeNode(val=left[0])
        root.right = None if not right else TreeNode(val=right[0])
        self.bst(root.left, left)
        self.bst(root.right, right)
