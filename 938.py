class Solution:
    def rangeSumBST(self, root, lo, hi):
        
        def dfs(node):
            if not node: return 0
            if node.val < lo: return dfs(node.right)
            if node.val > hi: return dfs(node.left)
            return node.val + dfs(node.left) + dfs(node.right)

        return dfs(root)
