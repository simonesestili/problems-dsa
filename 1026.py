class Solution:
    def maxAncestorDiff(self, root):
        self.v = 0

        def dfs(node, minn, maxx):
            if not node: return
            self.v = max(self.v, abs(node.val - minn), abs(node.val - maxx))
            minn, maxx = min(minn, node.val), max(maxx, node.val)
            dfs(node.left, minn, maxx)
            dfs(node.right, minn, maxx)

        dfs(root.left, root.val, root.val)
        dfs(root.right, root.val, root.val)
        return self.v
