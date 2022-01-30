class Solution:
    def searchBST(self, root, val):

        def search(node):
            if not node: return None
            if val < node.val: return search(node.left)
            elif val > node.val: return search(node.right)
            return node

        return search(root)

