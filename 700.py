class Solution:
    def searchBST(self, root, val):
        while root and root.val != val:
            root = root.left if val < root.val else root.right
        return root
