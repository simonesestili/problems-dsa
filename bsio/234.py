class Solution:
    def solve(self, root):
        self.res = float('-inf')

        def dfs(node):
            if not node: return 0
            l, m, r = dfs(node.left), node.val, dfs(node.right)
            self.res = max(self.res, l + m + r, m)
            return m + max(l, r)

        dfs(root)
        return self.res

