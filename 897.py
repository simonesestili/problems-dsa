class Solution:
    def increasingBST(self, root):

        def inorder(node):
            if node:
                yield from inorder(node.left)
                yield node
                yield from inorder(node.right)
        
        dummy = tail = TreeNode()
        for node in inorder(root):
            node.left = None
            tail.right = node
            tail = tail.right

        return dummy.right
