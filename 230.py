class Solution:
    def kthSmallest(self, root, k):

        def inorder(node):
            if node:
                yield from inorder(node.left)
                yield node.val
                yield from inorder(node.right)

        for i, val in enumerate(inorder(root)):
            if i+1 == k:
                return val

        return -1
