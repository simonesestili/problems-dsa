class Solution:
    def rangeSumBST(self, root, lo, hi):
        self.total = 0

        def dfs(node):
            if not node: 
                return
            if lo <= node.val <= hi:
                self.total += node.val
                dfs(node.left)
                dfs(node.right)
            elif node.val < lo:
                dfs(node.right)
            else:
                dfs(node.left)

        dfs(root)
        return self.total
