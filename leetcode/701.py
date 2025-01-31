class Solution:
    def insertIntoBST(self, root, val):

        def ins(node):
            if not node: return TreeNode(val)
            if val < node.val: node.left = ins(node.left)
            else: node.right = ins(node.right)
            return node

        return ins(root)
