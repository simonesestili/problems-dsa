class Solution:
    def preorderTraversal(self, root):
        vals = []

        def dfs(node):
            if node is None: return
            vals.append(node.val)
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return vals
