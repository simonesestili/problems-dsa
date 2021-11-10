class Solution:
    def preorderTraversal(self, root):
        self.vals = []

        def dfs(node):
            if not node:
                return
            self.vals.append(node.val)
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return self.vals
