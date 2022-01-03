class Solution:
    def findLeaves(self, root):
        self.depths = {}
        n = self.depth(root)
        self.ans = [list() for _ in range(n)]

        def dfs(node):
            if not node: return
            self.ans[self.depths[node] - 1].append(node.val)
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return self.ans

    def depth(self, root):
        if not root: return 0
        self.depths[root] = 1 + max(self.depth(root.left), self.depth(root.right))
        return self.depths[root]
