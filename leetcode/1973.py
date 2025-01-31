class Solution:
    def equalToDescendants(self, root):
        self.count = 0

        def dfs(node):
            if not node: return 0
            desc = dfs(node.left) + dfs(node.right)
            self.count += node.val == desc
            return node.val + desc

        dfs(root)
        return self.count
