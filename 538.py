class Solution:
    def convertBST(self, root):
        self.total = 0

        def dfs(node):
            if not node: return
            dfs(node.right)
            self.total += node.val
            node.val = self.total
            dfs(node.left)

        dfs(root)
        return root
