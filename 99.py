class Solution:
    def recoverTree(self, root):

        def inorder(node):
            if node:
                yield from inorder(node.left)
                yield node
                yield from inorder(node.right)

        prev = left = right = None
        for node in inorder(root):
            if prev and prev.val > node.val:
                left = left if left else prev
                right = node
            prev = node

        left.val, right.val = right.val, left.val
