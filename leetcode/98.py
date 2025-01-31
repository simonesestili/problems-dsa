class Solution:
    def isValidBST(self, root):

        def valid(node, lo=float('-inf'), hi=float('inf')):
            if not node: return True
            if not lo < node.val < hi: return False
            return valid(node.left, lo, node.val) and valid(node.right, node.val, hi)

        return valid(root)
