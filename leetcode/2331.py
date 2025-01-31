class Solution:
    def evaluateTree(self, root):

        def dfs(node):
            if node.val in (0, 1):
                return node.val
            if node.val == 2:
                return dfs(node.left) | dfs(node.right)
            return dfs(node.left) & dfs(node.right)

        return dfs(root)
