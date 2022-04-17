class Solution:
    def convertBST(self, root):

        def inorder(node):
            if node:
                yield from inorder(node.right)
                yield node
                yield from inorder(node.left)

        total = 0
        for node in inorder(root):
            node.val += total
            total = node.val

        return root
