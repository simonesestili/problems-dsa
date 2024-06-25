class Solution:
    def bstToGst(self, root):
        self.total = 0

        def dfs(node):
            if node is None: return
            dfs(node.right)
            self.total += node.val
            node.val = self.total
            dfs(node.left)

        dfs(root)
        return root

