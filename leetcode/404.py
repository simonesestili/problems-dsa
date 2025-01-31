class Solution:
    def sumOfLeftLeaves(self, root):
        self.ans = 0

        def dfs(node, side):
            if not node:
                return
            if not node.left and not node.right:
                self.ans += node.val if side == -1 else 0
            dfs(node.left, -1)
            dfs(node.right, 1)

        dfs(root, 0)
        return self.ans
