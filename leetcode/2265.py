class Solution:
    def averageOfSubtree(self, root):
        self.count = 0

        def dfs(node):
            if not node: return 0, 0
            lsum, lcnt = dfs(node.left)
            rsum, rcnt = dfs(node.right)
            msum, mcnt = lsum + rsum + node.val, lcnt + rcnt + 1
            self.count += node.val == msum // mcnt
            return msum, mcnt

        dfs(root)
        return self.count
