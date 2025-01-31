class Solution:
    def trimBST(self, root, lo, hi):
        
        def trim(node):
            if not node: return node
            if node.val < lo: return trim(node.right)
            if node.val > hi: return trim(node.left)
            node.left, node.right = trim(node.left), trim(node.right)
            return node

        return trim(root)
