class Solution:
    def deleteNode(self, root, key):
        if not root:
            return None

        if key == root.val:
            if not root.left:
                return root.right

            if not root.right:
                return root.left

            if root.left and root.right:
                curr = root.left
                while curr.right:
                    curr = curr.right
                root.val = curr.val
                root.left = self.deleteNode(root.left, root.val)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            root.right = self.deleteNode(root.right, key)

        return root
